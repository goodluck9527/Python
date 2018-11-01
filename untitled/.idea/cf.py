#_*_ coding: utf-8 _*_
import ReadFilesName
import os
import sys
import codecs
from chardet import detect

def get_now():
    # get the path now
    return os.getcwd()

def get_father(cwd):
    # get the father path now
    father_path = os.path.dirname(cwd)
    return father_path

def get_dir(cwd):
    # list all files in the path
    files_name = os.listdir(cwd)
    return files_name

def get_name():
    # get the name of the paragram
    return os.path.basename(sys.argv[0])


def read_files_name():
    cwd  = get_now()
    files = get_dir(cwd)
    return files

# f = open("2001_2013年我国煤矿瓦斯爆炸事故基本特征与发生规律探讨_刘建胜.pdf", 'r')
# print f.readline()

files = read_files_name()
for f in files:
    print f
# for file in files:
#     print file.decode('gbk')
#
# f = codecs.open(files[0].decode('gbk'), 'r', 'gbk')
# print f.name
