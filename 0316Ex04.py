# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:09:41 2021

@author: user
"""
'''
#一維串列
#刪除
number = [1,2,3,4,5,6,7,8,9]
del number[0] #刪除所引值0的值
print(number)
del number[1:6:2] #刪除print後的索引值1.3.5
print(number)
'''
#二維串列
data = [[1,2,3],[10,'A'],['A','B','C']]
  #外圍     0       1           2
print(data[1][0]) #印出外圍索引值1裡的索引值0
print(data[2][2]) #印出外圍索引值2裡的索引值2

for d in data:   #此時d轉為一維串列
    for i in d:
        print(i) #把一維串列裡的數字依序印出來
    print('-'*20)#把一維串列的數字分隔開
