#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 6-1 人

people = {
    'first_name': 'Rory',
    'last_name': 'Giles',
    'age': '33',
    'city': 'Los Angeles',
}

print(people['first_name'])
print(people['last_name'])
print(people['age'])
print(people['city'])

# 6-2 喜欢的数字
nums = {
    'Hulda': 2,
    'Yvonne': 54,
    'Christine': 66,
    'Uriah': 168,
    'Myra': 256,
}

print("Hulda " + str(nums['Hulda']))
print("Yvonne " + str(nums['Yvonne']))
print("Christine " + str(nums['Christine']))
print("Uriah " + str(nums['Uriah']))
print("Myra " + str(nums['Myra']))

# 6-3 词汇表
vocabulary ={
    'ram': '随机存取存储器',
    'cpu': '中央处理器',
    'wifi': '无线局域网',
    'disk': '硬盘',
    'redis': '内存数据库',
}

print(
    "ram: " + vocabulary['ram'] + "\n",
    "cpu: " + vocabulary['cpu'] + "\n",
    "wifi: " + vocabulary['wifi'] + "\n",
    "disk: " + vocabulary['disk'] + "\n",
    "redis: " + vocabulary['redis']
    )