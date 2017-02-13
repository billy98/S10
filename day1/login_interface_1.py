#!/usr/bin/env python
# -*- coding:utf8 -*-
import os
import sys
#

userfile = file('user.txt', 'r+')
userlist = []
userdict = {}
#是否存在用户文件,有的话执行,没有的话退出.
if os.path.isfile("user.txt"):
    pass
else:
    print '没有定义用户文件!'
    sys.exit
#userfile.readlines()
for userline in userfile:
    useritem = userline.strip()
    #生成系统用户列表
    value_useritem = useritem.split(';')
    #基本判断条件取出
    value_username = value_useritem[0].strip()
    value_passwd = value_useritem[1].strip()
    lock_value = int(value_useritem[-1])
    logincount_value = int(value_useritem[-2])
    #生成用户名列表
    userdict[value_username] = {'name':value_username, 'pwd':value_passwd, 'lockcount':logincount_value, 'locknum':lock_value}

flag = 'Ture'
counter = 0
while flag :
    username = raw_input('请输入用户名:')
    userpasswd = raw_input('密码:')
    #判断是否是系统用户
    if username not in userdict.keys() :
        print '没有这个用户!'
        break;
    elif userdict[username]['locknum'] == 0 and userdict[username]['lockcount'] < 3 :
        if userpasswd == userdict[username]['pwd'].strip() :
            print '欢迎登陆!!'
            break
        else:
            counter += 1
            userdict[username]['lockcount'] += 1
            userfile = file('user.txt', 'w+')
            for t in userdict.values():
                wuserlist = [str(t['name']), str(t['pwd']), str(t['lockcount']), str(t['locknum'])]
            # wuserlist = t.values()
                wuserlist_str = ';'.join(wuserlist)
                #userfile.seek(0)
                userfile.write(wuserlist_str + '\n')
            if counter > 2 :
                print '密码输入三次错误,退出.'
                break;
    else:
        print '帐户已经被锁定!'
        sys.exit('请联系管理解锁.')
    continue;
userfile.close()