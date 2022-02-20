# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 23:07:30 2022

@author: hongo
"""

multiple=[1234, 1234, 131521, 12341, 1231221, 112341, 243212]
def func(n):
    multiple=[]
    count=0
    for i in range(len(n)):
        if(n[i]/10>9):
            multiple.append(n[i])
    for i in range(len(multiple)):
        if(str(multiple[i])[0]==str(multiple[i])[-1]):
            count+=1
    return count
print(func(multiple))