#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 10-6 加法运算
try:
    first_number = input("First number: ")
    second_number = input("Second number: ")
    sums = int(first_number) + int(second_number)
    print(sums)
except ValueError:
    print("Please enter a number!")


# 10-7 加法计算器
while True:
    try:
        first_number = input("First number: (input 'q' to quit)")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        total: int = int(first_number) + int(second_number)
    except ValueError:
        pass
    else:
        print(total)


# 10-8 猫和狗
file_01 = 'cats.txt'
file_02 = 'dogs.txt'
try:
    with open(file_01, 'r') as f_obj:
        print(f_obj.read())
    with open(file_02, 'r') as f_obj:
        print(f_obj.read())
except FileNotFoundError:
    print("File does not exist!")


# 10-9 沉默的猫和狗
file_01 = 'cats.txt'
file_02 = 'dogs.txt'
try:
    with open(file_01, 'r') as f_obj:
        print(f_obj.read())
    with open(file_02, 'r') as f_obj:
        print(f_obj.read())
except FileNotFoundError:
    pass


# 10-10 常见单词
filename = 'OurDomesticBirds.txt'
try:
    with open(filename, 'r') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("File does not exist.")
else:
    print(contents.lower().count('the'))
