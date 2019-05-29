#python3
#encoding = utf-8
# @author: Du-Jia
# 2019-03-18

############################################################
# Tips: 
# turtle.circle(radius, extent=None, steps=None)
# Parameters: 
# radius – a number
# extent – a number (or None)
# steps – an integer (or None)
# 
# Help:
# This code contains some demo for the 8th class, teacher
# who use it can run it by uncomment different part code,
# and the content and purpose are writed in the subtitle.
# 
# All the method which teachers need to know:
#   1. turtle.circle(radius, extent, steps)
#   2. turtle.color(string)
#   3. turtle.home()
#   4. turtle.left()
#   5. turtle.right()
#   6. turtle.done()
#   7. turtle.setx(x)
#   8. turtle.sety(y)
#############################################################

import turtle

turtle.Turtle().screen.delay(0)


## Bind the pen
t = turtle.Pen()

## hide the arrow of turtle
t.hideturtle()

# ## [1] Part 1, radius
# ## How to draw a circle with circle() and argument radius
# t.color("blue")
# t.circle(25)
# t.circle(50)
# t.circle(100)

# ## Draw in another side
# t.color("blue")
# t.circle(-25)
# t.circle(-50)
# t.circle(-100)

# ## Draw circle with different radius and angels
# for degree in [0, 90, 180, 270]:
#     t.left(degree)
#     for radius in range(10, 100, 5):
#         t.circle(radius)


# ## [2] Part 2, extent
# ## Using extent to dipict curves
# t.color("green")
# t.circle(100, 120)

# ## A demo using extent
# for extent in range(10, 360, 10):
#     t.penup()
#     t.home()
#     print(t.heading())
#     t.left(extent)
#     t.pendown()
#     t.circle(100, 120)

# for extent in range(10, 370, 10):
#     t.penup()
#     t.home()
#     t.left(extent)
#     t.pendown()
#     t.circle(-100, 120)


## [3] Part 3, steps
## Draw polygons with the third argument
## ! Show a polygon one by one.
# ## 
# t.color("red")
# t.circle(100, steps=3)
# ## rectangle
# t.color("purple")
# t.circle(100, steps=4)
# ## more
# t.color("blue")
# t.circle(100, steps=5)
# # 
# ## The many steps, The more the polygon is clear to a circle
# t.color("black")
# t.circle(100, steps=6)
# t.color("black")
# t.circle(100, steps=12)
# t.color("black")
# t.circle(100, steps=24)

# ## Demo for steps
# for degree in [0, 90, 180, 270]:
#     t.left(degree)
#     radius = 100
#     for steps in [3,4,5,6,12,24]:
#         t.circle(radius, steps=steps)

# ## [4] Part 4. Draw circle in for loop
# step = 3
# for extent in range(0,361):
#     t.forward(step)
#     t.left(1)

## [5] Part 5. Set the center of circle
## You can learn how to control the center of circle, 

# ## Set the position of center
# x = 100
# y = 100

# for radius in range(5, 105, 5):
#     ## set the center
#     t.penup()
#     t.setx(x)
#     t.sety(y)
#     t.right(90)
#     t.forward(radius)
#     t.left(90)
#     t.pendown()

#     ## draw the circle
#     t.circle(radius)

#     ## move the pen back
#     t.penup()
#     t.left(90)
#     t.forward(radius)
#     t.right(90)

## The end
turtle.done()