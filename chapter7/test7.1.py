#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 7-1 汽车租赁
ask_car = input("What kind of car would you like to rent?: ")
print("Let me see if I can find you a " + ask_car)

# 7-2 餐馆订位
ask_guest = input("Hello, how many people are there in your party? ")
ask_guest = int(ask_guest)

if ask_guest > 8:
    print("There is no empty table")
else:
    print("Free table")

# 7-10 10的整数倍
prompt = input("Please enter a number: ")
prompt = int(prompt)

if prompt % 10 ==0:
    print("An integer multiple of 10")
else:
    print("NO integer multiple of 10")