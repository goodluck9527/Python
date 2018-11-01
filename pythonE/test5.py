#coding = utf-8
import codecs
a = open('test.txt', 'w')
b = open('《红楼梦》中四十回.txt','r')
t2 = b.readlines()
a.write("速度发货速度放缓")
a.close()
a = codecs.open('test.txt', 'r')
t = a.read()
