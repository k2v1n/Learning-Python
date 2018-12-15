#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 8-6 城市名
def city_country(city, country):
    """返回城市和所属的国家"""
    res = (city.title() + ' ' + country.title())
    return res

print(city_country('santisao','chile'))
print(city_country('macao','china'))
print(city_country('san francisco','America'))

# 8-7 专辑
def make_album(sinager, album,count=''):
    """返回歌手名字和专辑名"""
    if count:
        music_album = {'singer': sinager, 'album': album, 'count': count}
    else:
        music_album = {'singer': sinager, 'album': album}
    return music_album

print(make_album('Michael Joseph Jackso','Got to Be There'))
print(make_album('Adele Laurie Blue Adkins','19'))
print(make_album('张学友','Smile'))
print(make_album('张学友','Smile',11))

# 8-8 用户的专辑
while True:
    print("\nPlease enter singer name and album name")
    print("(enter 'q' at any time to quit)")
    s_singer = input("Singer: ")
    if s_singer == 'q':
        break
    s_album = input('Album: ')
    if s_album == 'q':
        break
    res = make_album(s_singer,s_album)
    print(res)
