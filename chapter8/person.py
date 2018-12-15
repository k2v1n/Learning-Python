#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def build_person(firstname, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': firstname, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(firstname, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': firstname, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix',age=16)
print(musician)
