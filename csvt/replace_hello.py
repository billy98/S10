#coding:utf8
#把a.t中的hello替换为billy并保存结果到文件a2.t中
import re
f = file('a.t','r')
L = f.read()
H = re.sub('hello','billy',L)
f.close()

c = file('a2.t','w')
c.write(H)
c.close()
