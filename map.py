from functools import reduce
def str2float( string ):
##    将字符串转化为列表
    strs = list(string)
##    找到小数点在列表中的位置以确定小数的位数
    index = strs.index('.')
##    从列表中移除小数点方便对字符进行转化
    strs.remove('.')
##    将字符转化为整数列表
    st1 = (list)(map(lambda x: int(x), strs))
##    切分整数部分
    zh = st1[:index]
##    切分小数部分并且翻转
    fl = st1[index:]
    fl.reverse()
##    求出整数部分
    sum_zh = reduce(lambda x, y: x * 10 + y, zh)

##    6 * 0.001 + 5 * 0.01 + 4 * 0.1 = (((6 * 0.1) + 5 ) * 0.1 + 4) * 0.1
##   求出小数部分 
    sum_fl = 0.1 * reduce(lambda x, y: x * 0.1 + y, fl)
##  返回整个浮点数
    return sum_zh + sum_fl
