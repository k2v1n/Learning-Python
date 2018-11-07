#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nums = [1,2,3,4,5]
#nums =range(1,5)

for i in range(len(nums)):
    #print('需循环',i)
    for j in range(i+1, len(nums)):
        #print(nums[i],nums[j])
        pass

d = {}
nums = [1,3,5,7,9]

for i ,num in enumerate(nums):
    d[num] = i
    #print(d)


for x in d:
    pass


print('Hello World')
