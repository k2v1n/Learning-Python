#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 10-3 访客

filename = 'guest.txt'
name = input("Please enter your name: ")
with open(filename, 'a') as file_object:
    file_object.write(name)

# 10-4 访客名单
filename = 'guest_book.txt'
while True:
    name = input("Please enter your name: (type 'q' to exit)")
    if name == 'q':
        break
    print("Hello, " + name + ' !')
    with open(filename, 'a') as file_object:
        file_object.write(name + '\n')

# 10-5 关于编程的调查
filename = 'languages.txt'
while True:
    language = input("What is your favorite programming reason? (type 'q' to exit)")
    if language == 'q':
        break
    with open(filename, 'a') as file_object:
        file_object.write(language + '\n')
