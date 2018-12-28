#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers: object = json.load(f_obj)


print(numbers)
