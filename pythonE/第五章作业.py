##5.1田字格
def drawLine(chr1, chr2, n):
       print('\n')
       for i in range(n * 5 + 1):
               if i % 5 == 0:
                       print("{}".format(chr1), end = '')
               else :
                       print("  {}  ".format(chr2), end = '')
def drawTian(n):
	for i in range(5 * n + 1):
		if i % 5 == 0:
			drawLine('+', '-', n)
		else:
			drawLine('|', ' ', n)
drawTian(6)

##5.3
##def isNum(num):
##    if type(num) == type(1):
##        return True
##    elif type(num) == type(1.0):
##        return True
##    elif type(num) == type(1 + 2j):
##        return True
##    else : return False

##5.5
##def multi(*a):
##    b = 1
##    for i in a:
##        b *= i
##    return b

##5.7
##def move(n ,sou, tar):
##    print ("移动第%d号盘子：%s - > %s" % (n, sou, tar))
##def hannuota(n, x, y, z):
##    if n == 1:
##        move(1, x, z)
##    else :
##        hannuota(n-1, x, z, y)
##        move(n, x, z)
##        hannuota(n-1, y, x, z)
