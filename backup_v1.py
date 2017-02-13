#!/usr/bin/env python
#coding:utf-8

#Filename:      backup_v1.py
#author:        billy
#time:          2017-02-08

import os
import time

source= ['/test','/mnt']

target_dir='/script/python/'

target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'

zip_command="zip -qr '%s' %s" %(target,' '.join(source))


if os.system(zip_command) == 0:
    print 'backup seccussful to',target
else:
    print 'backup failed'