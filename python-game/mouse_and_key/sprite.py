import pygame
import random

keep_going = True
# 控制图像的位置
picx = 0
picy = 0
# 背景颜色
BLACK = (0, 0, 0)
# 帧数
FPS = 60
# 动画速率
timer = pygame.time.Clock()
# 鼠标状态
mousedown = False

pygame.init()
screen = pygame.display.set_mode([600, 600])
pic = pygame.image.load("smile.png")

sprite_list = pygame.sprite.Group()

class Smiley(pygame.sprite.Sprite):
    def __init__(self, pos, xspeed, yspeed):
        self.pos = (0, 0)
        self.xspeed = 1
        self.yspeed = 1

        pygame.sprite.Sprite.__init__(self)
        self.scale = random.randrange(5, 100)
        self.image = pic
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0] - self.scale // 2
        self.rect.y = pos[1] - self.scale // 2
        self.xspeed = xspeed
        self.yspeed = yspeed

    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.xspeed = - self.xspeed

        if self.rect.y <= 0 or self.rect.y > screen.get_height() - self.scale:
            self.yspeed = - self.yspeed


while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False

    screen.fill(BLACK)
    sprite_list.update()
    sprite_list.draw(screen)
    timer.tick(FPS)
    pygame.display.update()

    if mousedown == True:
        xspeed = random.randint(-5, 5)
        yspeed = random.randint(-5, 5)
        newSmiley = Smiley(pygame.mouse.get_pos(), xspeed, yspeed)
        sprite_list.add(newSmiley)

pygame.quit()