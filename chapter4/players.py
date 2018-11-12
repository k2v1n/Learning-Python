#!/usr/bin/env python3
# -*- coding: utf-8 -*-

players = ['charles','martina','michael','florence','eli']
print(players[0:3])

players = ['charles','martina','michael','florence','eli']
print(players[1:4])

# 没有指定索引，将从列表的开头开始
players = ['charles','martina','michael','florence','eli']
print(players[:4])

players = ['charles','martina','michael','florence','eli']
print(players[2:])

# 输出最后三名
players = ['charles','martina','michael','florence','eli']
print(players[-3:])


players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
