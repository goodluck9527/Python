#实现文本分词，借助结巴分词组件
import codecs
import jieba
#coding=utf-8
counts={}
def splitSentence(inputFile):
    f = open(inputFile,'r')    #以读的方式打开文件
    lines = f.readlines()
    f.close()
    for line in lines:      #按行读入文件内容
        line = line.strip()     #删除每行首尾可能出现的空格
        wordList = list(jieba.cut(line))      #用结巴分词，对每行内容进行分词
        print '/'.join(wordList) #将分词结果打印到屏幕上
        for w in wordList:        #词频统计
            counts[w]=counts.get(w,0)+1
    #for key in counts.keys():   #词频统计结果打印到屏幕上
     #   print key+':',counts[key]
            
splitSentence('a0.txt')
f=codecs.open("a0_out.txt",'w','utf-8')
for key in  counts.keys():
    f.write("%s:%d\r\n"%(key,counts[key]))
f.close()
