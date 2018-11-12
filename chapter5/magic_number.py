#!/usr/bin/env python3
# -*- coding: utf-8 -*-

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")


# and运算符
age_0 = 22
age_1 = 26

if (age_0 >= 21) and (age_1 >=21):
    print("True")

age_0 = 18
age_1 = 18

if (age_0 >= 21) or (age_1 >=21):
    print("True")
