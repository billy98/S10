#coding:utf8
#通过字典实现switch

from __future__ import division

x=3
y=2
operator='/'
result={
    '+':x+y,
    '-':x-y,
    '*':x*y,
    '/':x/y
    }
print result.get(operator)