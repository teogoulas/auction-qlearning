import random

import matplotlib.pyplot as plt
import numpy as np

from environment.action import Action
from environment.environment import Environment
from utils.constants import NUM_EPISODES, EXPLORATION_RATE, LEARNING_RATE, DISCOUNT_RATE, MIN_EXPLORATION_RATE, \
    EXPLORATION_DECAY_RATE

if __name__ == '__main__':
    environments = {0: Environment(), 1: Environment()}
    state_space_size = environments[0].action_space.n
    observation_space_size = environments[0].observation_space.n
    q_table = {
        0: np.zeros((observation_space_size, state_space_size)),
        1: np.zeros((observation_space_size, state_space_size))
    }
    q_table_all_episodes = {0: [q_table[0]], 1: [q_table[1]]}
    rewards_all_episodes = {0: [], 1: []}
    exploration_rate = EXPLORATION_RATE
    total_reward = {0: 0, 1: 0}

    for episode in range(0, NUM_EPISODES):
        state = {0: environments[0].reset(), 1: environments[1].reset()}
        done = False
        score = {0: 0, 1: 0}

        while not done:
            action = {}

            # Generate actions for each agent
            for agent in range(0, 2):

                # Exploration-exploitation trade-off
                exploration_rate_threshold = random.random()
                if exploration_rate_threshold >= exploration_rate:
                    action[agent] = np.argmax(q_table[agent][state[agent], :])
                else:
                    action[agent] = environments[agent].action_space.sample()

            for agent in range(0, 2):
                agent_action = Action(agent, action[agent], action[0 if agent == 1 else 1])
                n_state, reward, n_done, info = environments[agent].step(agent_action)
                agent_q = q_table[agent]
                q_table[agent][state[agent], action[agent]] = q_table[agent][state[agent], action[agent]] * (1 - LEARNING_RATE) + \
                                             LEARNING_RATE * (reward + DISCOUNT_RATE * np.max(q_table[agent][n_state, :]))

                score[agent] += reward
                done = n_done
                state[agent] = n_state

        exploration_rate = MIN_EXPLORATION_RATE if exploration_rate == MIN_EXPLORATION_RATE \
            else exploration_rate - EXPLORATION_DECAY_RATE

        for agent in range(0, 2):
            rewards_all_episodes[agent].append(score[agent])

    for agent in range(0, 2):
        plt.plot(rewards_all_episodes[agent])
        plt.savefig(f'rewards_agent{agent}.png')
