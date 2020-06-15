#!/usr/bin/env python3

age = 0

# Please see:
# https://www.tocode.co.il/bundles/python/lessons/10-exceptions?tab=article
# For another idea how to write this loop

while age == 0 or age < 0: 
    age = int(input("please provide your age: "))

print("your age in month would be :", age * 12)
