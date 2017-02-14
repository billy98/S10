#!/usr/bin/env python
#coding:utf-8

import os

print (os.name)
#指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。

print os.getcwd()
#函数得到当前工作目录，即当前Python脚本工作的目录路径。

print os.getenv('path')
#读取环境变量


os.putenv('linux', 'e:\linux')
print os.getenv('linux')

