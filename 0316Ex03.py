# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:28:06 2021

@author: user
"""
#串列練習
#複習0311Ex04刪除remove/pop
data = [100,1,3,70,60,30]
data.sort() #遞增排序,位子會改變
print(data)
data.sort(reverse=True) #遞減排序,位子會改變
print(data)

number = [80,70,90,1,3,5]
n = sorted(number)               #遞增排序完之後複製出來,不會影響原本的排序
print(n)                         #複製出來的
print(number)                    #原本的

n = sorted(number, reverse=True) #遞減排序完之後複製出來,不會影響原本的排序
print(n)                         #複製出來的
print(number)                    #原本的

for i in sorted(number): #遞增
    print(i)
