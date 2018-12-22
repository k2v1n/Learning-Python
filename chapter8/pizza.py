#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print("\nMakeing a " + str(size) +
          "-inch pizza with the followng toppings:")
    for topping in toppings:
        print("- " + topping)

def pizza():
    pass