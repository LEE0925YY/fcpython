# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:53:56 2021

@author: User
"""

#1.隨機取數1~49,取6個且整數,不可重複,並放入串列
import random
number = list()
while len(number) != 6:
    n = random.randint(1,49)
    if number.count(n) == 0:
        number.append(n)
print(number)

#2.[100,80,1,3,10,7]排序小到大(氣泡排序)
data = [100,80,1,3,10,7]
n = len(data)
for i in range(n-1):
    for x in range(n-i-1):
        if data[x] > data[x+1]:
            data[x],data[x+1] = data[x+1],data[x]
print(data)