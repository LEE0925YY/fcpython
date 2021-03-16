# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:56:36 2021

@author: user
"""

student = ['John','Peter','May']
while True:
    q = input('輸入查詢姓名:')
    if q == 'q':
        break
    if student.count(q) != 0:
        print('有這位學生:',q,student.index(q)) #後面顯示此學生索引值
    else:
        name = input('是否加入(Y/N):')
        if name == 'Y':
            student.append(q)
print('學生共有:',student)
