# Python学习笔记-基本数据类型（二）
### 表示方法
* `'` 如：
```
>>>str = 'asdfasd'
```
* `"` 如：
```
>>>str = "asdfa"
```
* `'''` *注意:`'''`内可以使用`'` 和 `"` 如：
```
>>> print '''
asdfasdfasf
''
""""
asdfasdf
'''

asdfasdfasf
''
""""
asdfasdf

>>> 
```
### 基本操作符
<table>
<tr>
<th>操作符</th>
<th>描述</th>
</tr>
<tr>
<td>x + y</td>
<td>连接两个字符串</td>
</tr>
<tr>
</tr>
<tr>
<td>x * n 或 n * x</td>
<td>复制n次x字符串</td>
</tr>
<tr>
<td>x in y</td>
<td>判断x是否是y的子串</td>
</tr>
<tr>
<td>str[i]</td>
<td>取下标处字符</td>
</tr>
<tr>
<td>str[start:end]</td>
<td>取start到end处字符，不包括end处</td>
</tr>
<table>
### 内置字符串函数
* len(x)
* str(x):返回任意类型x对应的字符串表示
* chr(x):返回Unicode编码对应的字符
* ord(x):返回x的Unicode编码
* hex(x):十六进制表示
* oct(x):八进制表示
* str.lower()
* str.upper()
```
>>> c = "asdfasdf"
>>> c.lower()
'asdfasdf'
>>> c.upper()
'ASDFASDF'
>>> 
```
* str.islower()
* str.isupper()
```
>>> c = "asdfasdf"
>>> c.islower()
True
>>> c.isupper()
False
```
