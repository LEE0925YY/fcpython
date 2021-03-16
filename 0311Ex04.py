# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:42:41 2021

@author: user
"""

#刪除(把裡面的元素拿掉)
student = ['John','May','Tom']
print(student)

#student.remove('May')
#student.remove('David')

student.pop() #移除索引值(index),若不輸入,則是移除最後一個
print(student)  #印出['John','May']

student.pop(0)
print(student) #印出['May','Tom']

n = student.pop(0) #取出不放回(會顯示出索引值位置的物件)
print(n)  #印出John 

