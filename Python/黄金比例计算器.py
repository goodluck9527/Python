#encoding=utf-8
#python3
import math

ratio = (math.sqrt(5) - 1) / 2

##Info 
print('黄金比例是: ' + str(ratio))

num = 1

def small_side(num):
    return num * ratio

def large_side(num):
    return num / ratio

print('Input the num you want to compute here:')

num = float(input())

print('Which side you want?(1: big, 2: small):')

choice = input()
print(choice, type(choice))

if choice == '1':
    print(large_side(num))
elif choice == '2':
    print(small_side(num))
else:
    print('Error!')

