#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""一个用户类"""

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

class Admin(User):
    """管理员类"""
    def __init__(self, first_name, last_name, privileges, *profile):
        super().__init__(first_name, last_name, profile)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        """显示管理员权限"""
        self.privileges.show_privileges()

class Privileges():
    """权限类"""
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """显示管理员权限"""
        for privilege in self.privileges:
            print(privilege)