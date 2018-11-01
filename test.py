# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:07:41 2017

@author: du_jia


"""

## 示例代码——如何使用BeautifulSoup库

url = 'http://www.baidu.com'

from bs4 import BeautifulSoup
import requests



r = requests.get(url)
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')
#print(soup.prettify())

## BeautifulSoup库的基本元素
"""
这段代码介绍对BeautifulSoup库的理解
关键词：标签，标签树，属性，html, xml
Tag, attribute
最常用的引用方式：
from bs4 import BeautifulSoup
或者
import bs4

BeautifulSoup类可以当作对应一个HTML/XML文档的全部内容

基本元素：
Tag
Attribute


"""

##获得tag标签
tag = soup.title.p
print(tag)
