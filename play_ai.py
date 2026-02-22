import pygame
import sys
import torch
import copy

from env.flappy_env import FlappyEnv
from policy import PolicyNet

pygame.init()

WIDTH = 288
HEIGHT = 512
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

policy = PolicyNet()
policy.load_state_dict(torch.load("best_model.pth"))
policy.eval()


env = FlappyEnv()
state = env.reset()

score = 0
best_score = 0
passed_pipe = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    prob = policy(state)
    action = 1 if prob.item() > 0.5 else 0

    state, reward, done = env.step(action)

    if not passed_pipe and env.pipe_x + 50 < 50:
        score += 1
        passed_pipe = True

    if env.pipe_x > 50:
        passed_pipe = False


    if done:
        best_score = max(best_score, score)
        score = 0
        state = env.reset()


    screen.fill((135, 206, 250))

    bird_x = 50
    bird_y = int(env.bird_y)

    pipe_x = int(env.pipe_x)
    pipe_width = 50
    gap_center = int(env.pipe_gap_center)
    gap = int(env.pipe_gap)

    gap_top = gap_center - gap // 2
    gap_bottom = gap_center + gap // 2

    pygame.draw.circle(screen, (255, 255, 0), (bird_x, bird_y), 10)

    pygame.draw.rect(
        screen,
        (34, 139, 34),
        (pipe_x, 0, pipe_width, gap_top)
    )

    pygame.draw.rect(
        screen,
        (34, 139, 34),
        (pipe_x, gap_bottom, pipe_width, HEIGHT)
    )

    font = pygame.font.SysFont(None, 36)

    score_text = font.render(f"Score: {score}", True, (0,0,0))
    best_text = font.render(f"Best: {best_score}", True, (0,0,0))

    screen.blit(score_text, (10, 10))
    screen.blit(best_text, (10, 40))


    pygame.display.flip()
    clock.tick(60)
