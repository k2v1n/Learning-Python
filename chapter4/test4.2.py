#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 4-3数到20
for num in range(1,21):
    print(num)

# 4-4一百万
nums = list(range(1,1000001))
for value in nums:
    pass
    #print(value)

# 4-5 计算1~1000000的总和
nums = list(range(1,1000001))
print(min(nums))
print(max(nums))
print(sum(nums))

# 4-6 奇数
odd = list(range(1,21,2))
for value in odd:
    print(value)

# 4-7 3的倍数
num = list(range(3,31,3))
for value in num:
    print(value)

# 4-8 立方
nums = []
for value in range(1,11):
    nums.append(value**3)
print(nums)

# 4-9 立方解析
nums = [value**3 for value in range(1,11)]
print(nums)
