#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 7-4 披萨配料
while True:
    name = input("Please enter your pizza toppings：")
    if name == 'quit':
        break
    else:
        print("We add it to pizza " + name)

# 7-5 电影票
prompt = "Please enter your age: "
prompt += "or type ('quit') to exit."
active = True
while  active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            price = "free"
        elif age<= 12:
            price = "$10"
        else:
            price = "$15"
        print("Your ticket price is " + str(price))

# 7-6 三个出口
# while循环中使用条件测试来结束循环
age = ""
while age != 'quit':
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("free")
        elif age <=12:
            print("$10")
        else:
            print("$15")

# 使用break语句在用户输入'quit'时退出循环
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = "free"
        elif age<= 12:
            price = "$10"
        else:
            price = "$15"
        print("Your ticket price is " + str(price))

# 7-7 无限循环
x = 1
while x == 1:
    print(x)
