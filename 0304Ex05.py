# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 20:49:23 2021

@author: user
"""


# 迴圈:
# 初始值不可大於終止值。若是,預設值就要加-(負負得正的概念),如範例4
# range(10)     #(終止值)=(0,10)=初始值為0.間隔值都預設為1
# range(1,10)   #(初始值,終止值)間隔值預設為1
# range(1,10,2) #(初始值,終止值-1<意思是此數字不會印出來>,間隔值)
# 由最後(最正確版)range(1,10,2)往回推
# list:轉成串列(正列)
# 範例:
# print(list(range(10)))
# print(list(range(2,9)))
# print(list(range(1,10,2))) 印出:[1,3,5,7,9]
# print(list(range(10,1,-1)))


# for i in range(10):
#     print(i)
# print("程式執行完畢")

for i in range(1,10):
    if i % 2 == 0:
        print(i,"是偶數")
print("程式執行完畢")
