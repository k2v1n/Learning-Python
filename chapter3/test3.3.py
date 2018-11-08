#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3-8放眼世界

travel = ['France','USA','Spain','China','Italy']
print(travel)

# 按字母顺序打印
print(sorted(travel))
print(travel)

#按字母顺序相反打印
print(sorted(travel,reverse=True))
print(travel)

travel.reverse()
print(travel)

travel.reverse()
print(travel)

travel.sort()
print(travel)

travel.sort(reverse=True)
print(travel)

# 3-9晚餐嘉宾
list = []

list.append('bob')
list.append('jiessie')
list.append('benjamin')

print("Number of dinners:")
print(len(list))

# 3-10尝试使用多个函数
country = ['France','USA','Spain','China','Italy']
print(country)
print(len(country))
print(sorted(country))
print(sorted(country,reverse=True))
country.sort()
print(country)
country.reverse()
print(country)

# 3-11有意引发错误
# 索引错误
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles[5])

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles[3])

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles[-1])

motorcycles = []
print(motorcycles[-1])