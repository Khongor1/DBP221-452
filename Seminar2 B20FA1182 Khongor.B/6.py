# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:43:40 2022

@author: hongo
"""

list=[12, 16, 1, 1, 51, 51, 12, 3, 5, 16]
result=[]
for i in list:
    if i not in result:
        result.append(i)
print(result)