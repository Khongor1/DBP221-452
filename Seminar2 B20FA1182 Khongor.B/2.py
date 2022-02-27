# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:35:26 2022

@author: hongo
"""

s=("Mongoliin Ur Sad MASH olon BOLOh boltugaI")
jijig, tom=0 , 0
for i in s:
    if (i>="a" and i<="z"):
        jijig=jijig+1
    if (i>="A" and i<="Z"):
        tom=tom+1
print("The number of lower letter is:", jijig)
print("The number of upper letter is:", tom)