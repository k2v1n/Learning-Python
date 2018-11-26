#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 5-3 外星人颜色#1
alien_color = 'red'
if alien_color == 'green':
    spot = 5
    print("获得了" + str(spot) + "点经验.")
else:
    pass

# 5-4 外星人颜色#2
alien_color = 'red'
if alien_color == 'green':
    spot = 5
else:
    spot = 10
print("获得了" + str(spot) + "点经验.")

# 5-5 外星人颜色#3
alien_color = 'red'
if alien_color == 'green':
    spot = 5
elif alien_color == 'yellow':
    spot = 10
else:
    spot = 15
print("获得了" + str(spot) + "点经验.")

# 5-6人生的不同阶段
age = 26
if age < 2:
    print('婴儿')
elif 2 <= age < 4:
    print('蹒跚学步')
elif 4 <= age < 13:
    print('儿童')
elif 13 <= age < 20:
    print('青少年')
elif 20 <= age < 65:
    print('成年人')
else:
    print('老年人')

age = 66
if age < 2:
    print("He is a baby")
elif age < 4:
    print("He is studying walking now")
elif age < 13:
    print("He is a child")
elif age < 20:
    print("He is a teenage")
elif age < 65:
    print("He is an adult")
else:
    print("He is an old man")

# 5-7 喜欢的水果
favorite_fruits = ['banana','apple','strawberry']
if 'apple' in favorite_fruits:
    print('Your really like apples!')
if 'banana' in favorite_fruits:
    print('Your really like bananas!')
if 'watermelon' in favorite_fruits:
    print('Your really like watermelons!')
if 'strawberry' in favorite_fruits:
    print('Your really like strawberrys!')
if 'grape' in favorite_fruits:
    print('Your really like gappes!')
