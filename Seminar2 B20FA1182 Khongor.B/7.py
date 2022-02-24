# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:54:29 2022

@author: hongo
"""

def maximum(a, b, c):
    if (a>=b) and (a>=c):
        largest=a
    if(b>=a) and (b>=c):
        largest=b
    if(c>=a) and (c>=b):
        largest=c
    return largest
a=1
b=2
c=3
print(maximum(a, b, c))