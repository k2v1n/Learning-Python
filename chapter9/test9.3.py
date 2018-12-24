#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 9-6 冰淇淋小店
class Restaurant():
    """模拟餐馆"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化类属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐馆简介"""
        print("We " + self.restaurant_name.title() + " is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """餐馆营业中"""
        print("The restaurant is open now.")

    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self, number):
        """递增就餐人数"""
        self.number_served += number

class IceCreamStand(Restaurant):
    """冰淇淋小店子类"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """构造函数"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def get_ice_cream(self):
        """显示冰淇淋口味"""
        for flavor in self.flavors:
            print(flavor + " ice cream.")

flavors = ['vanilla', 'strawberry', 'peaunt']
IceCreamStand = IceCreamStand('McDonald', 'junk food', flavors)
IceCreamStand.get_ice_cream()

