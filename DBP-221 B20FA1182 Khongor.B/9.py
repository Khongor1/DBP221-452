# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 23:28:01 2022

@author: hongo
"""

num=[1, 1, 2, 3, 324, 1234, 1234, 134, 15, 1]
def func(n):
    n.pop(3)
    n.pop(5)
    n.pop(7)
    return n
print(func(num))