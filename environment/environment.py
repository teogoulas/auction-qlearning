import itertools

from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random

from environment.action import Action
from utils.constants import MAX_STEPS_PER_EPISODE

a = random.randint(0, 100)
b = random.randint(0, 100)

c = random.randint(-100, min(a, b))
d = random.randint(-100, min(a, b))


class Environment(Env):

    def __init__(self):
        self.action_space = Discrete(2)
        self.observation_space = Box(low=np.array([min(c, d)]), high=np.array([max(a, b)]), dtype=int)
        self.state = random.choice(list(itertools.product([0, 1], [0, 1])))
        self.episode_step = MAX_STEPS_PER_EPISODE

    def step(self, action: Action):
        self.state = (action.agent1_action, action.agent2_action)
        self.episode_step += -1

        if action.agent == 0:
            rewards = np.array([[a, c], [b, d]])
        else:
            rewards = np.array([[b, d], [a, c]])
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
