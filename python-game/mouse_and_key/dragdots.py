# encoding = utf-8
# from pygame import *
# from pygame.locals import *
import pygame


def main():
    # 颜色
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # 帧率
    timer = pygame.time.Clock()
    FPS = 60

    # 循环控制
    keep_going = True

    # 其他变量
    posx = 0
    posy = 0
    size = 10

    # 鼠标的状态
    mousedown = False

    pygame.init()
    # 设置屏幕
    screen = pygame.display.set_mode([800, 600])
    # 设置标题
    pygame.display.set_caption('Click and drag to draw')

    while keep_going == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousedown = True

            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False

        ## 画
        if mousedown == True:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, BLUE, pos, size)

        ## 擦除
        if mousedown == False:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, BLACK, pos, size)

        timer.tick(75)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()