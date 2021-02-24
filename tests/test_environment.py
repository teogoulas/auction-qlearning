from environment.action import Action
from environment.environment import Environment

from utils.constants import NUM_EPISODES

env = Environment()
for episode in range(0, NUM_EPISODES):
    state = env.reset()
    done = False
    score = 0

    while not done:

        action = Action(0, env.action_space.sample() - 1, env.action_space.sample() - 1)
        n_state, reward, done, info = env.step(action)
        score += reward

    print(f"Episode: {episode} Score: {score}")
