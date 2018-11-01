## 用Python来实现线性插值方法
## 来自《工程问题的C语言实现》
## 2017 07 26

## 存入初始数据
temp = [72.5,78.1,86.4,92.3,110.6,111.5,109.3,110.2,110.5,109.9,110.2]
time = [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]
#### 线性插值函数
## 使用线性插值的方法估算某一个时间点的温度值并且输出
## 输入： 时间点
## 输出： 温度值（带符号的温度值<摄氏>）
def Linear_get_temp(t):
        temp_of_t = None
        for i in range(len(time) - 2):
            if(time[i] <= t <= time[i+1]):
                temp_of_t = temp[i] + (t - time[i]) *( temp[i+1] - temp[i]) / (time[i+1] - time[i])
        return temp_of_t

## 使用线性插值法估算某一个温度值出现的时间点（可能有多个）并且输出
## 输入： 温度值

## 输出： 时间列表
def Linear_get_time(t):
        temp_of_t = []
        for i in range(len(time) - 2):
            if(time[i] <= t <= time[i+1]):
                temp_of_t.append(time[i] + (t - temp[i]) *( time[i+1] - time[i]) / (temp[i+1] - temp[i]))
        return temp_of_t
print('输入1将查询某时间节点的温度\n输入2查询某温度可能出现的时间\n输入-1结束该程序')
flag = eval(input())
while flag >= 0:
        print('输入1将查询某时间节点的温度\n输入2查询某温度可能出现的时间')
        flag = eval(input())
        if flag == 1:
                in_time = input("请输入要查询的时间点\n")
                t = Linear_get_temp(eval(in_time))
                print("the temreature in the time is : {}C".format(t))
        elif flag == 2 :
                in_time = input("请输入要查询的温度值\n")
                t = Linear_get_time(eval(in_time))
                print("the temreature in the time is : {}".format(t))
        else:
                print('\n\n输入1将查询某时间节点的温度\n输入2查询某温度可能出现的时间\n输入-1结束该程序\n')
                flag = eval(input())
                

