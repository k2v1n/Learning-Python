#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 存储所点披萨的的信息
pizza = {
    'crust': 'thick',
    'topping': ['mushrooms','extra cheese'],
    }

# 概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following topping:")

for topping in pizza['topping']:
    print("\t" + topping)