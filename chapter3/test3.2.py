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

list.insert(0,'peppa')
list.insert(2,'lisa')
list.insert(5,'pesi')

print("Large dining table " + list[0] + "," + list[1] + "," + list[2] + "," + list[3] + "," + list[4] + "," + list[5])

name = list.pop()
print(name + " Sorry, I can't invite you to dinner.")
name = list.pop()
print(name + " Sorry, I can't invite you to dinner.")
name = list.pop()
print(name + " Sorry, I can't invite you to dinner.")
name = list.pop()
print(name + " Sorry, I can't invite you to dinner.")

print(list)
print("Large dining table " + list[0])
print("Large dining table " + list[-1])

del list[0]
del list[-1]
print(list)
