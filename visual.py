import pygame
import sys
import random

pygame.init()

WIDTH = 288
HEIGHT = 512

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_y = HEIGHT // 2
bird_vel = 0
gravity = 0.25
flap = -4.5

pipe_x = WIDTH
pipe_w = 50
pipe_gap = 120
pipe_center = HEIGHT // 2
pipe_speed = 2

score = 0
scored = False


def reset_game():
    global bird_y, bird_vel
    global pipe_x, pipe_center
    global score, scored

    bird_y = HEIGHT // 2
    bird_vel = 0

    pipe_x = WIDTH
    pipe_center = random.randint(80, HEIGHT - 80)

    score = 0
    scored = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = flap

    # physics
    bird_vel += gravity
    bird_y += bird_vel

    pipe_x -= pipe_speed

    if pipe_x < -pipe_w:
        pipe_x = WIDTH
        pipe_center = random.randint(80, HEIGHT - 80)
        scored = False

    screen.fill((135, 206, 250))

    gap_top = pipe_center - pipe_gap // 2
    gap_bottom = pipe_center + pipe_gap // 2

    bird_x = 50

    if pipe_x < bird_x < pipe_x + pipe_w:
        if bird_y < gap_top or bird_y > gap_bottom:
            print("HIT!")
            reset_game()
            continue

    if bird_y <= 0 or bird_y >= HEIGHT:
        print("HIT GROUND!")
        reset_game()
        continue

    if not scored and pipe_x + pipe_w < bird_x:
        score += 1
        scored = True
        print("Score:", score)

    pygame.draw.circle(screen, (255, 255, 0), (bird_x, int(bird_y)), 10)

    pygame.draw.rect(screen, (34, 139, 34), (pipe_x, 0, pipe_w, gap_top))
    pygame.draw.rect(screen, (34, 139, 34), (pipe_x, gap_bottom, pipe_w, HEIGHT))

    pygame.display.flip()
    clock.tick(50)