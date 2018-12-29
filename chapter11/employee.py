#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Employee:
    """雇员类"""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = int(salary)

    def give_raise(self, amount=0):
        if amount:
            self.salary += amount
        else:
            self.salary += 5000
