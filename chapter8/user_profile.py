#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def build_proifle(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_proifle('Alex','KT',location='princeton',field='physics')
print(user_profile)
