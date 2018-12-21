#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('radish')
make_pizza('cheese','mushrooms','green peppers')

def make_pizza(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the followng toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('radish')
make_pizza('cheese','mushrooms','green peppers')

def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print("\nMakeing a " + str(size) +
          "-inch pizza with the followng toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16,'radish')
make_pizza(66,'cheese','mushrooms','green peppers')
