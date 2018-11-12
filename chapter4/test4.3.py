#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 4-10 切片

# 前3个元素
my_foods = ['pizza','falafel','carrot cake']
print("The first three items in the list are:")
print(my_foods[:3])

# 中间3个元素
my_foods = ['pizza','falafel','carrot cake','ice cream','steak']
print("\nThree items from the middle of the list are:")
print(my_foods[1:4])

print("\nThree last three items in the list are:")
print(my_foods[-3:])

# 4-11 你的比萨和我的比萨
my_pizzas = ['pizza','falafel','carrot cake']
friends_pizzas = my_pizzas[:]

my_pizzas.append('steak')
friends_pizzas.append('ice cream')

print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy favorite pizzas are:")
for friends_pizza in friends_pizzas:
    print(friends_pizza)

# 4-12 使用多个循环
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)
