#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 5-8 以特殊方式跟管理员打招呼

users = ['bob','jack','admin','lisa','benjamin']
for user in users:
    if user == 'admin':
        print("Hello " + user + ", would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")

# 5-9 处理没有用户的情形
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a status report?")
    else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-10 检查用户名
current_users = ['Ellen','Kingsley','Hume','Needham','Dickey']
new_users = ['Needham','Eveline','Emmie','Bell','Caroline']
low_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in low_current_users:
        print("This username: " + new_user + " has been used.")
    else:
        print("Username " + new_user + " is not used")

# 5-11 序数
numbers = [1,2,3,4,5,6,7,8,9]

for num in numbers:
    if num == 1 :
        print(str(num) + "st")
    elif num == 2 :
        print(str(num) + "nd")
    elif num == 3 :
        print(str(num) + "rd")
    else:
        print(str(num) + "th")
