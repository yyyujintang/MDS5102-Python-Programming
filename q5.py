#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   q5.py
@Time    :   2021/10/04 20:11:21
@Author  :   Tang Yujin 
@Version :   1.0
@Contact :   tangyujin0275@gmail.com
'''

def permute(num):
  length = len(num)
  if length == 1:
    return num
 
  result = []
  for i in range(length):
    res_list = num[:i] + num[i+1:]
    s = num[i]
    per_result = permute(res_list)
    if len(per_result) == 1:
      result.append(num[i:i + 1] + per_result)
    else:
      result += [[s] + j for j in per_result]
  return result

numbers = input("Input a list of numbers with , as inteval, eg: 3,5,6 :")
xlist = numbers.split(",")
xlist = [int(xlist[i]) for i in range(len(xlist))]
#numbers = [3,5,9]
#numbers = [1,0,5,6]
#numbers = [6]
print(len(permute(xlist)))
print(permute(xlist))