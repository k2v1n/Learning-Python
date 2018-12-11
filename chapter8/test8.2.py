#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 8-3 T恤
def make_shirt(code,word):
    """打印T恤尺码和字样"""
    print("Your T-shirt size is " + code + ". word is " + word.title())

make_shirt('28','hello world')
make_shirt(word='Less is more',code='16')

# 8-4 大号T恤
def make_shirt(code,word="I love Python"):
    """打印T恤尺码和字样"""
    print("Your T-shirt size is " + code + ". word is " + word.title())

make_shirt('L')
make_shirt('M')
make_shirt('S','hello world')

# 8-5 城市
def describe_city(city,county="china"):
    """打印城市及所属国家"""
    print(city.title() + " is in " + county + ".")

describe_city('guangzhou')
describe_city('shanghai')
describe_city('Philadelphia','US')
