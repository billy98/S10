# -*- coding:utf8 -*-
import os
import sys

username = 'billy'
passwd = 'sunfo'


while user_flag < 3:
    user_flag += 1
    _name = raw_input('username:').strip()
    if len(_name) == 0:
        continue
    if _name == username:
        pass
    else:
        print '''user:%s no find!''' %(_name)
        continue
    _pass = raw_input('password:').strip()
    if len(_pass) == 0:
        continue
    if _pass == passwd:
        print 'login success'
        break
    else:
        print '''password:%s is bad!''' %(_pass)
        continue


#os.remove(path)
#删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。