#!/usr/bin/env python
#coding:utf-8

#Filename:      backup_v2.py
#Author:        billy
#Time:          2017-02-08
#Email:         5884625@qq.com

import os
import time

source= ['/test','/mnt']

target_dir='/script/python/'

today=target_dir+time.strftime('%Y%m%d')

now=time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully create directory',today

target=today+os.sep+now+'.zip'

zip_command="zip -qr '%s' %s" %(target,' '.join(source))


if os.system(zip_command) == 0:
    print 'backup seccussful to',target
else:
    print 'backup failed'

'''
注意os.sep变量的用法——这会根据你的操作系统给出目录分隔符，即在Linux、Unix下它
是'/'，在Windows下它是'\\'，而在Mac OS下它是':'。使用os.sep而非直接使用字符，会使我们的
程序具有移植性，可以在上述这些系统下工作。