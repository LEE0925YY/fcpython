# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:48:07 2021

@author: User
"""

#1.遞減。寫出1234..9/123..8/123..7/../12/1(斷行)
for a in range(9,0,-1):
    for b in range(1,a+1):
        print(b,end='')
    print()
    
#2.巢狀菱形(最多7個*)
for a in range(1,5):
    print(' '*(4-a)+'*'*(2*a-1))
for a in range(3,0,-1):
    print(' '*(4-a)+'*'*(2*a-1))
    
#3.設ans=80,猜30,印出'介於30~100之間'；猜90,印出'介於30~90之間'
ans=80
l=1
h=100
while True:
    q  =  int(input("請輸入數字:"))
    if ans == 'q':
        print("答對了")
        break
    elif ans < q:
        print("猜錯，介於",l,"~",h,"之間:")
        h = q
    elif ans > q:
        print("猜錯，介於",l,"~",h,"之間:")
        l = q
print("答對了")