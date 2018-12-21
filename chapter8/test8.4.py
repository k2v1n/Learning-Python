#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 8-9 魔术师
magicians = ['Dillon','Locke','Funk']

def show_magicians(magicians):
    """打印列表中每个魔术师的名字"""
    for magician in magicians:
        print(magician)

#show_magicians(magicians)

# 8-10 了不起的魔术师
def make_great(magicians):
    """在每个魔术师的名字中都加入字样'the Great'"""
    count = 0
    while count < len(magicians):
        magicians[count] = "the Great" + magicians[count]
        count += 1

#make_great(magicians)
#show_magicians(magicians)

# 8-11 不变的魔术师
def make_great(magicians):
    """在每个魔术师的名字中都加入字样'the Great' 返回一个新的列表"""
    count = 0
    while count < len(magicians):
        magicians[count] = "the Great" + magicians[count]
        count += 1

    return magicians

new_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_magicians)
