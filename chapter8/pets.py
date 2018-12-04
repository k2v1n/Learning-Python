#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " +pet_name.title() + ".")

describe_pet("goodfish","bob")
describe_pet("cat","harry")

# 关键字实参
describe_pet(pet_name="harry",animal_type="dog")

# 默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " +pet_name.title() + ".")

describe_pet(pet_name='sarah')
