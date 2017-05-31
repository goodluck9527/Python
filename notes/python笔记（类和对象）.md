# 类和对象
### 引入
dir函数列举出一个对象的所有属性和方法
```
>>> dir("lkdjfa")
['__add__', '__class__', '__contains__', '__delattr__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__',
'__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', 
'_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith',
'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower',
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition','rsplit', 'rstrip', 'split',
'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
显示了一个字符串的所有可用的数据方法
* *以下划线开始头的名称是对象的私有属性，是不可见的 *
### 如何定义一个类
通过class 关键字声明， 与用def定义函数的方式类似
实例：
```
class Fridge:
    """This class implements"""
```
### 创建一个对象：
1. `f = Fridge()`语句调用类，并且创建一个对象
2. Python中的接口指的是提供给外界使用的方法`""" """`内的字符串是对类进行描述
3. 在类内可以定义方法，方式和定义一般方法一样。
4. 在类内，self指代这个类自身，类似于java中的this
5. 以下划线开头的方法不能直接从外部访问

