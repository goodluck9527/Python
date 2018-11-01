
4.1猜数游戏
from random import *
ans = randint(0, 9)
cnt = 0
b = eval(input("请输入你猜的数[0->9]："))
while True:
	cnt += 1
	if b > ans:
		print("遗憾，你猜的数太大了")
		b = eval(input("再尝试一次吧！（你可以继续游戏）"))
	elif b < ans:
		print("遗憾，你猜的数太小了")
		b = eval(input("你可以继续游戏！（在这里输入)"))
	else :
		print ("预测%d次，你猜对了!" % cnt)
		break

4.3
def gcb(a, b):
        if a < b : a ,b = b ,a
        r = a % b
        while r != 0:
                a = b
                b = r
                r = a % b
        return b

4.5猜数游戏
from random import *
ans = randint(0, 9)
cnt = 0
b = eval(input("请输入你猜的数[0->9]："))
try:
        while True:
                cnt += 1
                if b > ans:
                        print("遗憾，你猜的数太大了")
                        b = eval(input("再尝试一次吧！（你可以继续游戏）"))
                elif b < ans:
                        print("遗憾，你猜的数太小了")
                        b = eval(input("你可以继续游戏！（在这里输入)"))
                else :
                        print ("预测%d次，你猜对了!" % cnt)
                        break
except NameError:
       print("请输入一个整数") 

4.7
try:
    temp = input("请输入带符号的温度")
    if temp[-1] in ['f', 'F']:
        c = (eval(temp[:-1]) -32) / 1.8
        print ("{}c".format(c))
    elif temp[-1] in ['c', 'C']:
        c = eval(temp[:-1]) * 1.8 + 32
        print ("{:.2f}f".format(c))
except NameError:
    print ("请按照正确格式输入")
