#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = input("Please enter you name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name)

age = input("How old are you? ")
print(int(age))