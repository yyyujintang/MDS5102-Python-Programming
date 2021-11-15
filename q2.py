#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   q2.py
@Time    :   2021/10/04 12:20:29
@Finish  :   2021/10/04 13:20:29
@Author  :   Tang Yujin 
@Version :   1.0
@Contact :   tangyujin0275@gmail.com
'''
# Library Import
from math import sin
from math import cos
from math import tan

# Input
function = ["sin","cos","tan"]
f = input("Choose a function: sin cos tan :")
if f not in function:
    print("Please input the right function name!!!")
    # If the function name error, stop all following procedure
    exit()
a = input("Input the interval lower end points a :")
a_num = float(a)

b = input("Input the interval upper end points b :")
b_num = float(b)
if b_num<a_num:
    print("b can't be less than a!!!")
    # If b<a , stop all following procedure
    exit()

n = input("Input number of sub-intervals n :")
# str2float
n = float(n)
# float2int
n = int(n)

# Calculating
def integral(f,a,b,n):
    count = 0
    if f == "sin":
        for i in range (1,n+1):
            count += (b-a)/n*(sin(a+(b-a)/n*(i-1/2)))
    if f == "cos":
        for i in range (1,n+1):
            count += (b-a)/n*(cos(a+(b-a)/n*(i-1/2)))
    if f == "tan":
        for i in range (1,n+1):
            count += (b-a)/n*(tan(a+(b-a)/n*(i-1/2)))
    return count


# Output
output = integral(f,a_num,b_num,n)
print("The intergration of funtion %s between %s and %s with %d division is %s" % (f,a,b,n,output))

# 测试用例 sin 3 6.8 1000 WolframAlipha:-1.85939 本程序：-1.8593911056837171
# 测试用例 cos -1 9.2 300 WolframAlipha:1.06436 本程序：1.0644121673533695
# 测试用例 tan 1 3.8 1000 WolframAlipha:0.981238 本程序：1.1477655966684057
# 测试用例 tan 1 3.8 500 WolframAlipha:0.981238 本程序：0.34273630116758363
# 测试用例 tan 1 3.8 10000 WolframAlipha:0.981238 本程序：16.576331373716716