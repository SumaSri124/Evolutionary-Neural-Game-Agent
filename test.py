from env.flappy_env import FlappyEnv
from policy import PolicyNet

env = FlappyEnv()
policy = PolicyNet()

state = env.reset()
done = False

total_reward = 0
steps = 0

while not done:
    prob = policy(state)

    action = 1 if prob.item() > 0.5 else 0

    state, reward, done = env.step(action)

    total_reward += reward
    steps += 1

print("Episode finished")
print("Steps survived:", steps)
print("Total reward:", total_reward)