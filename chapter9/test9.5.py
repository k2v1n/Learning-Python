#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 9-13 使用OrderedDict
from collections import OrderedDict
vocabulary = OrderedDict()

vocabulary ={
    'ram': '随机存取存储器',
    'cpu': '中央处理器',
    'wifi': '无线局域网',
    'disk': '硬盘',
    'redis': '内存数据库',
    }

for key,value in vocabulary.items():
    print(key + ": " + value)

# 9-14 骰子
from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

die_0 = Die(10)
for i in range(10):
    die_0.roll_die()

die_1 = Die(20)
for i in range(10):
    die_1.roll_die()