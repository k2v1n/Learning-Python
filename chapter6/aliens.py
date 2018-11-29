#!/usr/bin/env python3
# -*- coding: utf-8 -*-

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'red', 'points': 15}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("Total number of aliens: " + str(len(aliens)))

# 修改前3个外星人的颜色、移动速度、点数
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 15}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
