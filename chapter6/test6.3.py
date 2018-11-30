#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 6-7 人
people_0 = {
    'first_name': 'Rory',
    'last_name': 'Giles',
    'age': '33',
    'city': 'Los Angeles',
}
people_1 = {
    'first_name': 'Oliver',
    'last_name': 'Wagner',
    'age': '12',
    'city': 'Ethiopia',
}
people_2 = {
    'first_name': 'Andre',
    'last_name': 'Franklin',
    'age': '26',
    'city': 'NJ',
}

people = [people_0,people_1,people_2]
for info in people:
    print(info)

# 6-8宠物
pet_0 = {'kind': 'gold retriever','master': 'bob'}
pet_1 = {'kind': 'pib bull','master': 'benjamin'}
pets = [pet_0,pet_1]
for pet in pets:
    print(pet)

# 6-9 喜欢的地方
favorite_places = {
    'Hannah': ['Canda','Thailand'],
    'Dave': ['Indonesia','Moscow','Iceland']
}

for name,places in favorite_places.items():
    print("\n" + name.title() + " like to go ")
    for place in places:
        print(place)

# 6-10 喜欢的数字
nums = {
    'Hulda': [1,4,7987],
    'Yvonne': [2,5652,82326,4],
    'Uriah': [168,568,2156,239],
}

for name,numb in nums.items():
    print(name + " like numbers: ")
    for num in numb:
        print("\t" + str(num))

# 6-11 城市
cities = {
    'New York': {
        'country': 'US',
        'population': 8622698,
        'fact': 'freedom'
    },
    'Hangzhou': {
        'country': 'CN',
        'population': 9460000,
        'fact': 'beauty'
    },
    'Moscow': {
        'country': 'RU',
        'population': 12000000,
        'fact': 'comfort'
    }
}

for city,info in cities.items():
    print( city + " is very " + info['fact'] +
           " population： " + str(info['population']) +
           " city impression: " + info['fact'])

# 6-12 扩展
pet_0 = {'kind': 'gold retriever','master': 'bob'}
pet_1 = {'kind': 'pib bull','master': 'benjamin'}
pets = {
    'a': pet_0,
    'b': pet_1,
}
for info in pets.values():
    print("pet " + info['kind'] + "'s master is " + info['master'])
