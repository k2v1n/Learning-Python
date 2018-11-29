#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 6-4 词汇表2
vocabulary ={
    'ram': '随机存取存储器',
    'cpu': '中央处理器',
    'wifi': '无线局域网',
    'disk': '硬盘',
    'redis': '内存数据库',
    }

for key,value in vocabulary.items():
    print(key + ": " + value)

vocabulary['list'] = '列表'
vocabulary['tuple'] = '元组'
vocabulary['dict'] = '字典'
vocabulary['sorted'] = '排序'
vocabulary['print'] = '打印'

for key,value in vocabulary.items():
    print(key + ": " + value)

# 6-5 河流
rivers = {
    'nile': 'egypt',
    'amazonas': 'brasil',
    'changjiagn': 'china',
}

for key,value in rivers.items():
    print("The " + key + " runs through " + value + ".")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

# 6-6 调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
survey = ['phil','benjamin','edward']

for name in survey:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for taking the poll.")
    else:
        print(name.title() + ", please take our poll!")
