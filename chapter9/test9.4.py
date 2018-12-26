#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 9-10 导入Restaurant类型
import restaurant
restaurant = restaurant.Restaurant('Mcdonald', 'junk food')
restaurant.describe_restaurant()

# 9-11 导入Admin类
#import user
#admin = user.Admin('Augustine', 'Geordie', ['a', 'b', 'c'])
#admin.show_privileges()

# 9-12 多个模块
from user import User
from admin import Admin, Privileges

admin = Admin('Augustine', 'Geordie', ['a', 'b', 'c'])
admin.show_privileges()
