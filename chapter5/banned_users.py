#!/usr/bin/env python3
# -*- coding: utf-8 -*-

banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", You can post a response if you wish.")