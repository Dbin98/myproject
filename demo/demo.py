#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/12/23 16:38
# @Author  :Alive
# @Site    :
# @File    :demo.py
# @Software:PyCharm
"""

print("我的年龄是：%d岁,国籍是：%s"%(21,"中国"))

print("www","baidu","com",sep=".")
print("www","baidu","com")


passworld = int(input("请输入密码"))
print("你输入的密码是：",passworld)
print("你输入的密码的类型：",type(passworld))

"""


#猜拳小游戏
import random
guess = input("请输入： 剪刀（0）、石头（1）、布（2）：")
if guess.isalpha():
    guess = input("请重新输入： 剪刀（0）、石头（1）、布（2）：")
guess = int(guess)
if guess>2 or guess < 0:
    guess = int(input("请重新输入： 剪刀（0）、石头（1）、布（2）："))
rad  = random.randint(0,2)
print("随机生成数字：",rad)
if guess == 0 :
    if rad ==0 :
        print("平局")
    elif rad == 1:
        print("你输了")
    else:
        print("你赢了")
elif guess == 1:
    if rad ==0 :
        print("你赢了")
    elif rad == 1:
        print("平局")
    else:
        print("你输了")
else:
    if rad == 0:
        print("你输了")
    elif rad == 1:
        print("你赢了")
    else:
        print("平局")

"""
#1-100求和
i = 1
sum = 0
max = 100
while i<=max:
    sum +=i
    i+=1
print("1到%d求和的值：%d"%(max,sum))
"""
"""
for i in range(1,10):
    for j in range(1,i+1):
        sum = i * j
        print("%d*%d=%d" % (i, j, sum),end=" ")
    print(" ")
"""
#打印99乘法表
"""
i=1
while i<=9:
    j=1
    while j<i+1:
        sum = i * j
        print("%d*%d=%d" % (i, j, sum), end=" ")
        j+=1
    print(" ")
    i+=1

"""





