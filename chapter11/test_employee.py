#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """测试雇员用例"""

    def setUp(self):
        self.employee = Employee('Chery', 'Parker', 6000)

    def test_give_default_raise(self):
        self.assertEqual(self.employee.salary, 6000)

    def test_give_custom_raise(self):
        self.employee.give_raise(100)
        self.assertEqual(self.employee.salary, 6100)

    def test_give_empty_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 11000)


unittest.main()
