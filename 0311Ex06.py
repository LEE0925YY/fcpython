# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 21:38:01 2021

@author: user
"""

num = [30,60,1,20,30,40,50,55]
total = sum(num)   #加總sum(串列裡面不可放字串)
ma = max(num) #最大
mi = min(num) #最小
print(total,ma,mi)

m = max(num[2:5]) #索引值2開始到5結束(5不能算)
print(m)
