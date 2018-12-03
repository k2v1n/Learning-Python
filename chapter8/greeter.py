#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def greet_user():
    """显示简单的问候语"""
    print('Hello!')

greet_user()

def greet_user(username):
    """显示简单的问候语"""
    print('Hello!' + username.title() + "!")

greet_user('sraah')