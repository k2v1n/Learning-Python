#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 8-12 三明治
def make_sandwich(*toppings):
    """对顾客点的三明治进行概述"""
    for topping in toppings:
        print("Your sandwich contains the following ingredients:")
        print("- " + topping)

make_sandwich('bacon')
make_sandwich('bacon','egg','ham sausage')
make_sandwich('bacon','egg','cheese')

# 8-13 用户简介
def build_proifle(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_proifle('Payne','Zechariah',country='China',city='Guangzhou',birth='1999')
print(my_profile)

# 8-14 汽车
def make_car(manufacturer,type,**infomation):
    """将汽车信息存储在字典中"""
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['type'] = type
    for key,value in infomation.items():
        car_info[key] = value
    return car_info

car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)
