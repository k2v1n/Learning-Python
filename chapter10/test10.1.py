#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 10-1 Python学习笔记
filename = 'learning_python.txt'

with open(filename) as file_object:
    print(file_object.read())

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# 10-2 C语言学习笔记
filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python','C'))
