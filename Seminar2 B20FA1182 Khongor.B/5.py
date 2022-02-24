# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:35:06 2022

@author: hongo
"""

total=0
element=0
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while(element<len(list)):
    total=total+list[element]
    element+=1
print("The sum of the elements is:", total)