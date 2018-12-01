#!/usr/bin/env python3
# -*- coding: utf-8 -*-

number = input("Enter a number, and I'll tell you if it's even ord odd: ")
number = int(number)

if number % 2 ==0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
