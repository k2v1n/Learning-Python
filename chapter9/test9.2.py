#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 9-4 就餐人数
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

    def get_number_served(self):
        """获取当前就餐人数"""
        print(self.number_served)

restaurant = Restaurant('Michelin starred', 'western food')

print(restaurant.number_served)
restaurant.set_number_served(666)
restaurant.get_number_served()
restaurant.increment_number_served(123)
restaurant.get_number_served()

# 9-5 尝试登录次数
class User():
    """描述用户信息的类"""
    def __init__(self, first_name, last_name, *profile):
        """初始化用户信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile
        self.login_attempts = 0

    def describe_user(self):
        """打印用户信息摘要"""
        print(self.first_name)
        print(self.last_name)
        print(self.profile)

    def greet_user(self):
        """个性化问候"""
        print("Hello " + self.first_name + " " + self.last_name + "!")

    def increment_login_attempts(self):
        """登录次数递增加一"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """清除登录次数"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """获取登录次数"""
        print(self.login_attempts)

new_user = User('xiaomign','chen')
new_user.get_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.get_login_attempts()
new_user.reset_login_attempts()
new_user.get_login_attempts()
