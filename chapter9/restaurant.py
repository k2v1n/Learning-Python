#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""一个模拟餐馆类"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """初始化类属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐馆简介"""
        print(self.restaurant_name.title() + " is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """餐馆营业中"""
        print("The restaurant is open now.")

    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self, number):
        """递增就餐人数"""
        self.number_served += number