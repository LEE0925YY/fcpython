# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:37:31 2021

@author: user
"""

data = [100,20,'John',3.14] #[索引值編號0,1,2,3...]
'''
print(data[2])

data[3] = 3.12 #改變data索引值
print(data)

#print(data[100]) 超出索引值範圍會出錯(out of range)
#從最後面往回推的索引值[-4,-3,-2,-1]
print(data[-1]) #3.12
print()

for i in range(4):
    print(data[i])
'''
#list裡的函數'len':計算串列裡面的個數
for i in range(len(data)):
    print(data[i])

print()

for d in data: #依序將data裡的直抓出來給d(跟函數的答案一樣,程式較精簡)
    print(d)
    
    
