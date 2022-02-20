# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 23:27:59 2022

@author: hongo
"""

num=[1234, 1234, 131521, 12341, 1231221, 112341, 243212]
def func(n):
    return list(dict.fromkeys(n))
print(func(num))