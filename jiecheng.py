##def count(n):
##      断言，保证输入值为正数
##    assert n >= 0

##        定义阶乘函数
##    def f(x):
##        if x == 1 or x == 0: return 1
##        else : return x * f(x - 1)

##      阶乘求和
##    sum = 0
##    for i in range(1, n + 1):
##        sum += f(i)

##        返回结果
##    return sum




## 生成一个文件：
f = open("dictionary.txt", 'w+')

##  给出各月的天数：(平年)
days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]

## 定义判断闰年的工具函数
def isrun(year):
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: return True
	else : return False
	
## 用三层循环来写入日期
## 第一层为年份循环
for year in range(1990, 2018):
	if year == 2017:
		days_per_month = [31,28,31,30,31,30,31,3]
		month_len = 8
	else:
		month_len = 12
##	判断是否是闰年,是则改变二月日期
	if isrun(year): days_per_month[1] = 29
	else: days_per_month[1] = 28

	for month in range(month_len) :
##		将日期写入文件
		for day in range(days_per_month[month]):
			f.write("{}-{}-{}\n".format(year,month + 1,day + 1))
			
## 关闭文件资源
f.close()

## TEST
f = open("dictionary.txt", 'r')
dic = f.readlines()
for i in range(100):
	print (dic[i])
f.close()


