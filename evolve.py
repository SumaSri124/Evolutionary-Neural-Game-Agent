from env.flappy_env import FlappyEnv
from policy import PolicyNet
import torch
import copy
def evaluate_network(policy):
    env = FlappyEnv()

    state = env.reset()
    done = False

    total_reward = 0
    steps = 0

    MAX_STEPS = 400

    while not done and steps < MAX_STEPS:
        prob = policy(state)

        action = 1 if prob.item() > 0.5 else 0

        state, reward, done = env.step(action)

        total_reward += reward
        steps += 1

    return total_reward, steps


def mutate(policy):
    for param in policy.parameters():
        noise=torch.randn_like(param) * 0.5
        param.data+=noise

if __name__ == "__main__":
    population =[PolicyNet() for _ in range(6)]
    best_ever_reward = -99999
    best_ever_policy = None

    for generation in range(20):
        print("Generation",generation)
        best_reward = -99999
        best_policy = None

        for pn in population:
            reward, steps = evaluate_network(pn)
            print("reward: ",reward)
            if reward>best_reward:
                best_reward=reward
                best_policy=pn
        print("best reward  this generation",best_reward)
        
        if best_reward > best_ever_reward:
            best_ever_reward = best_reward
            best_ever_policy = copy.deepcopy(best_policy)
            torch.save(best_ever_policy.state_dict(), "best_model.pth")
            print("✅ Saved new best model:", best_ever_reward)

                
        #next generation
        new_population = []
        new_population.append(copy.deepcopy(best_policy))
        for _ in range(6):
            child = copy.deepcopy(best_policy)
            mutate(child)
            new_population.append(child)
        print("New population created:", len(new_population))
        population=new_population
        #test
        #reward, steps = evaluate_network(new_population[0])
        # print("Child test reward:", reward)