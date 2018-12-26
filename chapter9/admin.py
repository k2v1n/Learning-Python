#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""一个管理员类"""

from user import User

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