#!/usr/bin/env python3
# -*- coding: utf-8 -*-

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if  message != 'quit':
        print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program."
active = True
message = ""
while active:
    message = input(prompt)
    if  message == 'quit':
        active = False
    else:
        print(message)


