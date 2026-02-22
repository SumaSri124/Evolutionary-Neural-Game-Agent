from env.flappy_env import FlappyEnv

env = FlappyEnv()

state = env.reset()
print("State:", state)

for t in range(30):
    action = 0 
    next_state, reward, done = env.step(action)
    print(f"t={t}, state={next_state}, reward={reward}, done={done}")
    if done:
        print("Game Over at timestep:", t)
        break
