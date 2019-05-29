# encoding = utf-8

import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going = True
GREEN = (0, 255, 0)
radius = 50

timer = pygame.time.Clock()

FPS = 10
BLACK = (0, 0, 0)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    screen.fill(BLACK)
    for index in range(100):
        pos_x = random.randint(0, 800)
        pos_y = random.randint(0, 600)
        size = random.randint(0, 255)
        color = (random.randint(0, 800) % 255, random.randint(0, 600) % 255, size)
        pygame.draw.circle(screen, color, (pos_x, pos_y), size // 10)

    timer.tick(FPS)
    # pygame.draw.circle(screen, GREEN, (100,100), radius)
    pygame.display.update()

pygame.quit()