#coding:utf8
#查找a.t文件中hello的个数

import re
count=0
f1=file('a.t','r')
for x in f1.readlines():
    L = re.findall('hello',x)
    if len(L)>0:
        count+=len(L)
print  count
f1.close()
