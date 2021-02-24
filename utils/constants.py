NUM_EPISODES = 150
MAX_STEPS_PER_EPISODE = 20
LEARNING_RATE = 0.01  # a parameter
DISCOUNT_RATE = 0.9  # gamma parameter

EXPLORATION_RATE = 1
MAX_EXPLORATION_RATE = 1
MIN_EXPLORATION_RATE = 0
EXPLORATION_DECAY_RATE = 0.01


A_REWARD = 1  # random.randint(-1, 1)
B_REWARD = 1  # random.randint(-1, 1)

C_REWARD = -1  # random.randint(-1, min(A_REWARD, B_REWARD))
D_REWARD = -1  # random.randint(-1, min(A_REWARD, B_REWARD))
