#!/usr/bin/env python3
# -*- coding: utf-8 -*-

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

# 改变第一个元素的值
motorcycles[0] = 'ducati'
print(motorcycles)

# 列表末尾添加元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles .append('kawasaki ')
print(motorcycles)

# 空列表赋值
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 在列表任意位置插入元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

# 使用del删除元素
motorcycles = ['honda','yamaha','suzuki']

del motorcycles[0]
print(motorcycles)

# pop方法删除元素
motorcycles = ['honda','yamaha','suzuki']
poped_motorcycles = motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print("购买的最后一辆摩托车是：" + last_owned.title() + ".")

# 弹出列表任意位置的元素
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print("购买的第一辆摩托车是：" + first_owned.title() + ".")

# 根据值删除元素
motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive + " is too expensive for me.")

