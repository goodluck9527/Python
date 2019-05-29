import pygame
import random

pygame.init()
screen = pygame.display.set_mode([600, 600])
keep_going = True

pic = pygame.image.load("smile.png")

# 控制图像的位置
picx = 0
picy = 0

# 背景颜色
BLACK = (0, 0, 0)

# 帧数
FPS = 60

# 动画速率
timer = pygame.time.Clock()

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    picx += 1
    picy += 1

    pygame.display.update()

    ## 设置刷新频率
    timer.tick(FPS)

pygame.quit()