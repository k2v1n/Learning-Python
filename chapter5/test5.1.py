#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 5-1 条件测试

car = 'nissan'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car == 'Nissan'? I predict False.")
print(car.title() == 'Nissan')

print("\nIs car == 'bmw'? I predict False.")
print(car == 'bmw')

print("\nIs car == 'jeep'? I predict False.")
print(car == 'jeep')

# 5-2 更多的条件测试

str = 'apple'
num1 = 10
num2 = 15
test_list = ['a','b','c']

print(str == 'apple')
print(str.lower() == 'Apple')
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

print(num1 > 15 and num2 > 22)

print(num1 > 15 or num2 < 22)

print('A' in test_list)

print('A' not in test_list)
