#!/bin/python

import random

tam = random.randrange(3, 7)
nums = []

for i in range(tam) :
    nums.append(random.randrange(1, 5))

print nums

def no_reps(nums) :
    total = 0
    for i in range(len(nums)) :
        if nums.count(nums[i]) == 1:
            total = total + nums[i]
    return total

print no_reps(nums)

