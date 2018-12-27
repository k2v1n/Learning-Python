#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_words(f):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(f) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + f + " does not exist."
        # print(msg)
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + f + " has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']
for filename in filenames:
    count_words(filename)
