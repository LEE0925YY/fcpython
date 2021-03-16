# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:21:02 2021

@author: user
"""
'''
fruits = ['apple,','banana','orange','apple','cherry','apple']
q = input("搜尋水果:")
if fruits.count(q) == 0:
    print("找不到,q")
else:    
    c = fruits.count(q) #c決定迴圈要跑幾次
    ind = 0
    for i in range(c):
        ind = fruits.index(q,ind) #ind:從0開始算
        print(ind,'索引位置')
        ind += 1
'''
student = [] #空的串列
while True:
    st = input('輸入新增學生名(q)') #若輸入q,則會break離開,所輸入的值會形成一串列
    if st =='q':
        break
    student.append(st) #append新增(物件)
print(student)

#中途插入
student.insert(1, 'John') #在索引值1的地方插入John
print(student)
