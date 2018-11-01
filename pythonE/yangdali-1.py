import jieba
def splitSentence(inputFile):
    sumWords = 0
    counts={}
    f = open(inputFile,'r')    #以读的方式打开文件
    lines = f.readlines()
    f.close()
    for line in lines:      #按行读入文件内容
        line = line.strip()     #删除每行首尾可能出现的空格
        wordList = list(jieba.cut(line))      #用结巴分词，对每行内容进行分词
##        print ('/'.join(wordList)) #将分词结果打印到屏幕上
        for w in wordList:        #词频统计
            sumWords += 1         ##记录当前出现词汇的总个数
            counts[w]=counts.get(w,0)+1
    return counts, sumWords

def sortByvalue(D):  ##定义一个以键值排序的函数
    a=[]    ##创建一个列表存储排序后的字典 
    for key in D.keys(): a.append((key,D[key]))
    ##将字典的键和键值封装成一个元组存入a中
    L = sorted(a,key=lambda s:s[1],reverse=True)
    return L

def tongji(L, endTo): ##L表示已经排序过后的列表， endTo是需要统计的词的个数，个数越高，结果越精确
    a = []  ##存储经过统计的列表
    cnt = 0 ##计数器
    for i in L:
        if not i[0] in ["。", '，', '；', '’', '“' ,'”','：' ,'！', '？', '不', ' 了' ] :  ##排除符号
            if len(i) >= 2: ##排除词汇长度小于1的词
                cnt+= 1
                a.append(i)
            if cnt > endTo : break; ##达到统计要求后终止循环
    return a

def turnToRate(a, su):
    b = []
    for tur in a:
        c = []
        c.append(tur[0])
        c.append(tur[1] / su * 100)
        b.append(c)
    return b

##def display(L):
##    for d in L:   #词频统计结果打印到屏幕上
##        print (d[0]+':',d[1])
def contrast(a, b):
    print("前八十回" + "\t\t\t" + "后四十回")
    for i in range(len(a)):
        print(a[i], end = "\t")
        print(b[i])

def analyze(qian, hou):
    wq, wh = [], []
    for i in qian:
        wq.append(i[0])
    for i in hou:
        wh.append(i[0])
    cnt = 0
    same = []
    for i in wq:
        if i in wh:
            cnt += 1
            same.append(i)
    print("相同的词个数为：" + str(cnt) + "\n相同的词为" + str(same))
    print("使用频率对比")
    con = []
    con.append(["相同词语","在前八十回中使用频率",
                "在后四十回中使用频率", "词频差"])
    for i in same:
        tem = []
        for j in qian:
            if i in j:
                tem.append(i)
                tem.append(j[1])
                for j in hou:
                    if i in j:
                        tem.append(j[1])
                        tem.append(tem[1] - tem[2])
        con.append(tem)
    for i in con:
        print(i)

        
data_80, sum_words_1=splitSentence('红楼梦前八十回.txt')
data_sort_80 = sortByvalue(data_80)
##display(L)
data_40, sum_words_2 = splitSentence('红楼梦后四十回.txt')
data_sort_40 = sortByvalue(data_40)
data_80_tong = tongji(data_sort_80, 20)
data_40_tong = tongji(data_sort_40, 20)
data_80_rate = turnToRate(data_80_tong,sum_words_1)
data_40_rate = turnToRate(data_40_tong,sum_words_2)
contrast(data_80_rate, data_40_rate)
analyze(data_80_rate, data_40_rate)
##print(data_80_rate)
##print(data_40_rate)

##f=open("红楼梦前八十回out.txt",'w')
##for d in  L:
##    f.write("%s:%d\r\n"%(d[0],d[1]))
##f.close()


##cnt = 0
##for i in S:
##    if i[0] not in ["。", '，', '；', '’', '“' ,'：' ,'！', '？', '不', ' 了' ]:
##        if len(i) >= 2:
##            cnt += 1
##            hou.append(i)
##        if cnt > 20:  break;



