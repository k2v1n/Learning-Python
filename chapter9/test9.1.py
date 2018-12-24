#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 9-1 餐馆
class Restaurant():
    """包含餐馆名称和烹饪类型的类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化类属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """餐馆简介"""
        print("We " + self.restaurant_name.title() + " is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """餐馆营业中"""
        print("The restaurant is open now.")

restaurant = Restaurant('Pizza Hut', 'warm')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 三家餐馆
restaurant2 = Restaurant('Home Bar & Restaurant', 'western food')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Michelin starred', 'western food')
restaurant3.describe_restaurant()

# 9-3 用户
class User():
    """描述用户信息的类"""
    def __init__(self, first_name, last_name, *profile):
        """初始化用户信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile

    def describe_user(self):
        """打印用户信息摘要"""
        print(self.first_name)
        print(self.last_name)
        print(self.profile)

    def greet_user(self):
        """个性化问候"""
        print("Hello " + self.first_name + " " + self.last_name + "!")

user_1 = User("luffy","munch","a")
user_2 = User("Hubery","Doherty","b")
user_1.describe_user()
user_2.describe_user()
user_1.greet_user()
user_2.greet_user()
