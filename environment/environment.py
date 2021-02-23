import itertools
import random

import numpy as np
from gym import Env
from gym.spaces import Discrete, Box

from environment.action import Action
from utils.constants import MAX_STEPS_PER_EPISODE, A_REWARD, C_REWARD, B_REWARD, D_REWARD


class Environment(Env):

    def __init__(self):
        self.action_space = Discrete(2)
        self.observation_space = Box(low=np.array([min(C_REWARD, D_REWARD)]), high=np.array([max(A_REWARD, B_REWARD)]),
                                     dtype=int)
        self.state = random.choice(list(itertools.product([0, 1], [0, 1])))
        self.episode_step = MAX_STEPS_PER_EPISODE

    def step(self, action: Action):
        self.state = (action.agent1_action, action.agent2_action)
        self.episode_step += -1

        if action.agent == 0:
            rewards = np.array([[A_REWARD, C_REWARD], [D_REWARD, B_REWARD]])
        else:
            rewards = np.array([[B_REWARD, D_REWARD], [C_REWARD, A_REWARD]])
        reward = rewards[action.agent1_action][action.agent2_action]

        if self.episode_step <= 0:
            done = True
        else:
            done = False

        info = {}

        return self.state, reward, done, info

    def reset(self):
        self.state = random.choice(list(itertools.product([0, 1], [0, 1])))
        self.episode_step = MAX_STEPS_PER_EPISODE
        return self.state

    def render(self, mode='human'):
        # implement visualizations
        pass
