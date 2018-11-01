第六章作业
6.1随机密码生成
import random
def createPd(lengthOfPd):
    apl = []
    for i in range(65, 65 + 26):
        apl += chr(i)
        apl += chr(i).lower()
    for i in range(0, 10):
        apl += str(i)
    pd = []
    for i in range(lengthOfPd):
        pd += random.choice(apl)
    return pd
password = createPd(8)
print(password)

6.3
def isRepeated(a):
    tem = set(a)
    return len(a) != len(tem)

6.5生日悖论
import random
def display():
    same = 0
    the_whole = 0
    birth = []
    for i in range(24):
        birth.append(random.randint(0, 365))
    for i in range(24):
        for j in range(i + 1, 24):
            the_whole += 1
            if birth[i] == birth[j]:
                same += 1
    print("生日悖论演示：总人数为{}, 生日相同次数{},\n 测试次数{}, 生日相同的概率{}".format(23, same, the_whole, same/the_whole * 100))

6.6红楼梦人物出场分析
import jieba
def getName(filename, len_of_present):
    f = open(filename)
    text = f.read()
    ##去除标点符号
    ch = '，。、‘；、！@#%……&*（）——+“”’‘·？》《\t\n：'
    for i in ch:
        text = text.replace(i, ' ')
    word = text.split()
    words = {}
    for line in word:
        for i in jieba.lcut(line):
            words[i] = words.get(i, 0) + 1
    ##这里的words是一个字典类型的数据，下面将它转换为列表类型
    words_list = list(words.items())
    words_list.sort(key=lambda x: x[1], reverse=True)
    final = []
    len_of_present=50
    cnt = 0
    for i in words_list:
        if len(i[0]) >= 2:
            cnt += 1
            final.append(i)
            if cnt > len_of_present: break
    return final

def iterator(lt):
    for i in lt:
        print (i)

out = '只这那丫东不出自没怎两进咱你告知他众说姑一听如就回起我大什'
def main():
    cnt = 0
    name = input("请输入你要统计的文件名(包括文件后缀):\n")
    name_list = getName(name, 50)
    iterator(name_list)
    for i in out:
        for j in name_list:
            if i == j[0][0]:
                print(i + '\n' + j[0][0])
                cnt+=1
                name_list.remove(j)
    iterator(name_list)
    for i in name_list:
        if i[0][0] in out or i[0] in ex:
            cnt += 1
            print(cnt)
            name_list.remove(i)
    print(name_list)
    print(cnt)
    return name_list

