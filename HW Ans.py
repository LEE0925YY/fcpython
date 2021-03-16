# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:14:52 2021

@author: user
"""

#0309作業1-遞減
for a in range(9,0,-1):
    for b in range(1,a+1):
        print(b,end='')
    print()

#0309作業2-菱形解1
for a in range(1,5): #1-4
    print(' '*(4-a)+'*'*(2*a-1)) #空白*3+'*'*1(上半部)
for a in range(3,0,-1):
    print(' '*(4-a)+'*'*(2*a-1)) #下半部
print() #菱形解2
for i in range(1,8,2):
    print(('*'*i).center(7)) #center:在中間
for i in range(5,0,-2):
    print(('*'*i).center(7))
#0311作業2-氣泡排序(小到大)
data = [100,80,1,3,10,7]
n = len(data) #長度(索引值有幾個)
for i in range(n-1): #執行次數6-1=5,i=[0,1,2,3,4](因最後最大數字上去之後就不會跟他比了)
    for x in range(n-i-1): #此行最重要 #6-0-1=5 跑0.1.2.3.4
        if data[x] > data[x+1]: #若索引值1>2
            data[x],data[x+1] = data[x+1],data[x] #索引值前後交換
print(data)
#相鄰兩值比較，若前比後大，前就跟後交換位子
#0311作業1-大樂透取值
import random
number = list()
while len(number) != 6: #到6就離開(要把0算進去,到5總共有6個數字)
    n = random.randint(1,49)
    if number.count(n) == 0:
        number.append(n)
print(number) #今天教的解法

import random
number = [0,0,0,0,0,0]
i = 0
while number.count(0) != 0:
     n = random.randint(1,49)
     if number.count(n) == 0:
        number[i] = n
        i += 1
print(number)


