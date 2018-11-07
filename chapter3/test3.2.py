#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list = []

list.append('bob')
list.append('jiessie')
list.append('benjamin')

print("Inviting dinner with " + list[0].title() + "," + list[1] + "," +list[2])

non_list = list.pop(0)
list.insert(0,'anna')
print("Unable to go to appointment " + non_list)
print("Inviting dinner with " + list[0] + "," + list[1] + "," +list[2])

list.append('lisa')
list.append('pesi')
list.insert(0,'peppa')

print("Large dining table " + list[0] + "," + list[1] + "," + list[2] + "," + list[3] + "," + list[4] + "," + list[5])
