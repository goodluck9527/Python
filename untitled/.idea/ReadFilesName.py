# _*_ coding: utf-8 _*_
import os
import sys

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
