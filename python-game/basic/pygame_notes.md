# How to use PyGame

## Demo

	import pygame

	pygame.init()
	screen = pygame.display.set_mode([800,600])

	keep_going = True
	GREEN = (0, 255, 0)
	radius = 50


	while keep_going:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            keep_going = False

	        pygame.draw.circle(screen, GREEN, (100,100), radius)
	        pygame.display.update()

	pygame.quit()

- PyGame的基本用法
	+ 初始化： pygame.init()
	+ 创建显示窗口： pygame.display.set_mode([800, 600])
	+ 持续绘制游戏屏幕： 使用while循环
	+ RGB颜色
	+ 处理交互事件: for循环
	+ 清除pygame模块，关闭窗口，正常退出。

- PyGame的坐标系统：
	+ 