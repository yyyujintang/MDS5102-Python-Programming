#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   q3.py
@Time    :   2021/10/04 14:06:44
@Finish  :   2021/10/04 14:35:44
@Author  :   Tang Yujin 
@Version :   1.0
@Contact :   tangyujin0275@gmail.com
'''
# Statement Initialization
list = [False]*100

# 初始：全关闭
# 第一个人：全打开
# 第二个人：从第二个柜子开始，把2，4，6，8，10双数全关闭
# 第三个人：从第三个柜子开始，交换每个第三个状态
# 第四个人：从第四个柜子开始，交换每个第四个状态
# 第五到一百人：重复

def switch(str):
    if str == False:
        return True
    else:
        return False

def change_every_n(n):
    # 第二个人从第二个柜子开始，2，4，6，8关闭
    # 把n作为loop的步长
    # range(x, y, step)
    # 如果是第三个柜子，其索引为2
    for i in range(n-1,100,n):
        list[i]= switch(list[i])

# 1st-100th loop,这里输入的是人的次序数，从1到100
for i in range(1,101):
    change_every_n(i)

# Print
print_list = []
for i,flag in enumerate(list):
    if flag==True:
        # 比如索引3，是第四个柜子
        print_list.append(i+1)
print(print_list)

