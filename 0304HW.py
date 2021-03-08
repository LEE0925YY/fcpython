# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:41:43 2021

@author: User
"""

#1.請利用for range計算1~50之間,偶數和及奇數和。
total = 0
for i in range(2,51,2):
    total += i
print("偶數總和:",total)

total = 0
for i in range(1,50,2):
    total += i
print("奇數總和:",total)

#2.請利用for range印出 2,4,6,8。
for i in range(2,10,2):
    print(i, end="")
    if i != 8:
        print(",", end="")
