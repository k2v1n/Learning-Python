#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from city_functions import region


class CityTestCase(unittest.TestCase):
    """测试城市和国家的返回值"""

    def test_city_country(self):
        city_county_name = region('santiago', 'chile')
        self.assertEqual(city_county_name, 'Santiago, Chile')

    def test_city_country_population(self):
        city_county_name = region('santiago', 'chile', '5000000')
        self.assertEqual(city_county_name, 'Santiago, Chile - population 5000000')


unittest.main()
