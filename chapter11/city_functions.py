#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def region(city, country, population=''):
    if population:
        res = city.title() + ", " + country.title() + " - population " + population
    else:
        res = city.title() + ", " + country.title()
    return res