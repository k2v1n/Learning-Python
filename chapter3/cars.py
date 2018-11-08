#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 按字母顺序排列
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

# 按字母顺序相反排列
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw','audi','toyota','subaru']
print("original list:")
print(cars)

print("\n sorded list:")
print(sorted(cars))
print(sorted(cars,reverse=True))

print("\noriginal list:")
print(cars)

# 倒着打印列表(永久性修改)
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

# 打印列表长度
cars = ['bmw','audi','toyota','subaru']
print(len(cars))
