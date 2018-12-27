#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 10-6 加法运算
try:
    first_number = input("First number: ")
    second_number = input("Second number: ")
    sum = int(first_number) + int(second_number)
    print(sum)
except ValueError:
    print("Please enter a number!")
