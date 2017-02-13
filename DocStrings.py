#!/usr/bin/env python
#coding:utf-8

#Filename:      DocStrings.py
#author:        billy

def printMax(x,y):
    '''print the maximun of two numbers.


    The two values must be integers.'''
    x=int(x)
    y=int(y)
    if x>y:
        print x,'is maximun'
    else:
        print y,'is maximun'

print printMax(3,5)
print printMax.__doc__