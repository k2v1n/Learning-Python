#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from car import ElectricCar

car = ElectricCar('tesla', 'model s', 2016)
print(car.get_descriptive_name())
car.battery.describe_battery()
car.battery.get_range()
