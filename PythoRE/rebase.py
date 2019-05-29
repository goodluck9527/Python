#python3

import re
import os

global string
global result

with open('./test.txt', 'r', encoding='utf-8') as file:
    string = ''.join(file.readlines())
    # print(string)
    result = re.search('[0-9]', string)
    result.group()
    print(result.group(0))


