## 8-2
##Python题目1

#### 创建一个文件1.txt
##f = open("1.txt", 'w+')
##f.write('''This is my cat, my cat's name is betty.
##This is my dog, my dog's name is frank.
##This is my fish, my fish's name is George.
##This is my goat, my goat's name is adam.
##''')
##f.close()
##
#### 读取文件并且将my替换成为your
#### 读取文件并将文件内容存储到变量中
##file_1 = open("1.txt", 'r')
##content = file_1.readlines()
##
#### 用your替换my
##new_con = ''
##for i in content:
##    i = i.replace('my','your')
##    new_con += i
##file_1.close()
##
#### 新建文件并且输入内容
##file_2 = open("2.txt", 'w')
##file_2.write(new_con)
##file_2.close()

##Python 题目二
def decorator(F):
   def new_F():
       print(F.__class__.__name__)
       return F()
   return new_F

@decorator
def hello():
   print ("hello world!")

