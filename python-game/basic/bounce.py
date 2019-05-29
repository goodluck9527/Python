import pygame
import random

pygame.init()
screen = pygame.display.set_mode([600, 600])
keep_going = True

pic = pygame.image.load("smile.png")

# 控制图像的位置
picx = 0
picy = 0

# 移动速度
speedx = 3
speedy = 4

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

    picx += speedx
    picy += speedy

    if picx + pic.get_width() >= 600 or picx <= 0:
        speedx = -speedx
    if picy + pic.get_height() >= 600 or picy <= 0:
        speedy = -speedy

    # 重画背景
    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))

    # 更新图像
    pygame.display.update()
    ## 设置刷新频率
    timer.tick(FPS)

pygame.quit()