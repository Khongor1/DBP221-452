# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 23:52:46 2022

@author: hongo
"""

num = {'adsf': 1, '22':2, '21':1}
num1 = {'asf': 11, '2':22, '212':31}

num2 = dict(num, **num1)
print(num2)