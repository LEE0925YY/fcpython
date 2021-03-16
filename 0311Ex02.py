# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:29:06 2021

@author: user
"""

'''
number = [10,20,30,40,50,60,70]
print('前三項:', number[:3])
print('抓索引值2之後:', number[2:])
print('抓索引值1-4之後:', number[1:5])
print(number[-3:]) #往前抓,所以是抓後三個50,60,70
'''

student = ['John','Bill','Cherry','David','Bill']

ind = student.index('Bill') #學生的物件
print(ind) #印出索引值
#ind = student.index('Peter')
ind = student.index('Bill',2)
print(ind)

c = student.count('Bill') #count:數量
print(c)
c = student.count('Peter')
print(c)

