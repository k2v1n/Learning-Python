#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# 10-11 喜欢的数字
# filename = 'number.json'
# number = input('Please enter your favorite number: ')
# with open(filename, 'w') as f_obj:
#     num = json.dump(number, f_obj)
#
#
# with open(filename) as f_obj:
#     num = json.load(f_obj)
# print("I know your favorite number! It's " + num + '.')


# 10-12 记住喜欢的数字
# filename = 'number.json'
# try:
#     with open(filename) as f_obj:
#         num = json.load(f_obj)
#         print("I know your favorite number! It's " + num + '.')
# except FileNotFoundError:
#     number = input('Please enter your favorite number: ')
#     with open(filename, 'w') as f_obj:
#         num = json.dump(number, f_obj)


# 10-13 验证用户
def get_stored_username():
    """如果存储了用户名 就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户 并指出其名字"""
    username = get_stored_username()
    if username:
        ask = input("Is your "+ username + " ? (type N input new username)")
        if ask == 'N':
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
        else:
            print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()