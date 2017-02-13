#coding:utf8
import re

s = '''
hello billy
billy hello
haha billy
billy hehe
'''
r = r'^billy'
print re.findall(r,s)
print re.findall(r,s,re.M)


tel = '''
\d{3,4}
-?
\d{8}
'''
print re.findall(tel,'010-12345678')
print re.findall(tel,'010-12345678',re.X)

print '#'*40
#分组
k = '''
hhsdfh dsdhl hello src=billy yes jdolahk
ihoihj src=123 yes lhoih
hello src=python yes ksa
'''

r1 = r'hello src=.+ yes'
r2 = r'hello src=(.+) yes'

print re.findall(r1,k)
print re.findall(r2,k)

