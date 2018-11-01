import turtle 
def drawSnake(rad, angle, len, neckRad):
	turtle.seth(-40)
	for i in range(length):
		turtle.circle(radius, angle)
		turtle.circle(-radius, angle)
	