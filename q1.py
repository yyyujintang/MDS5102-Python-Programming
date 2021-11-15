#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   q1.py
@Time    :   2021/10/04 00:13:43
@Finish  :   2021/10/04 00:57:03
@Author  :   Tang Yujin 
@Version :   1.0
@Contact :   tangyujin0275@gmail.com
'''
# Library Import
import math

# Get Input
number = input("Input A Number Between 0 and 500：")
number = int(number)

# prime Judgement
def is_prime(n):
    if n < 2: 
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# palindromic Judgement
def is_palindromic(num):
    flag = True
    num = str(num)
    for i in range(len(num)//2):
        if num[i] == num[len(num)-i-1]:
            continue
        else:
            flag = False
    return flag
        
# emirp Judgement
def is_emirp(num):
    flag = False
    if is_palindromic(num) == False:
        if is_prime(num) == True:
            flag = True
    return flag

# get reverse number
def num_reverse(n):
    s = str(n)    
    s = s[-1::-1] 
    n = int(s)    

    return n

# Acquire Satisfied Data
list = []
start = 10
while len(list)< number:
    if is_emirp(start) == True and is_emirp(num_reverse(start)) == True:
        list.append(start)
    start+=1
        

# Print
count= 0
for i in list:
    print(i, end=' ')
    count += 1 #开始计数
    if count % 10 == 0: #每10个换行
        print(end='\n')