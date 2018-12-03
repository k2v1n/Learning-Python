#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 7-8 熟食店
sandwich_orders = ['Bacon sandwich','Ham sandwich','Egg sandwiches']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your tuna sandwich " + current_sandwich)
    finished_sandwich.append(current_sandwich)

print("\nThe sandwich is ready: ")
for sandwich in finished_sandwich:
    print(sandwich)

# 7-9 五香烟熏牛肉
sandwich_orders = ['Ham sandwich','pastrami','Bacon sandwich','pastrami','pastrami']
finished_sandwich = []
print("partrami is sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    finished_sandwich = sandwich_orders

print(finished_sandwich)

# 7-10 梦想的度假胜地
travel = {}

while True:
    name = input("\nWhat is your name? ")
    city = input("If you cloud visit one place in the world, where would you go? ")
    travel[name] = city
    repeat = input("would you like to let anther person respond? (yes/no) ")
    if repeat == 'no':
        break


print("-----Resutls-----")
for name,city in travel.items():
    print(name + " like go to " + city + ".")
