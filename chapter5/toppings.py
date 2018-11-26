#!/usr/bin/env python3
# -*- coding: utf-8 -*-

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'peppeeroni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
