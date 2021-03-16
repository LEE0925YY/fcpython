# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:34:11 2021

@author: user
"""

#元祖Tuple(唯讀的串列,只能讀不能改)用小括弧
data = (10,'A',100,90)
print(type(data))
print(data[1])
#data[0]=99 #錯誤的(不能更改)
#元祖不能改,若要改,轉成新串列,再轉回元祖
newlist = list(data)
newlist[0]=99
print(newlist) #中括弧(可更改)
olddata = tuple(newlist)
print(olddata) #小括弧(不可更改)

#會自動轉回元祖的情況:一次給他多個數值
number = 1,2,3,4
print(number) #印出來就會是元祖

