#!/usr/bin/env python3

print("Please provide next details: ")
init = int(input("initial number of series: "))
val = int(input("the diff between the nums: "))
amount = int(input("amount of digits in series:"))
i = 0

while i  < amount:
    i = i + 1
    init = init + val

print("the sum of series is :",init)
