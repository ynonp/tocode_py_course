#!/usr/bin/env python3

nums = []
i = 0
while len(nums) <10:
    i = input(f"{len(nums)}) enter a num: ")
    nums.append(i)

print(f"the biggest num would be {max(nums)}")
