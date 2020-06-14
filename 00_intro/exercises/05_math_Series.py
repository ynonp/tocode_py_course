#!/usr/bin/env python3

print("Please provide next details: ")
init = int(input("initial number of series: "))
val = int(input("the diff between the nums: "))
amount = int(input("amount of digits in series:"))
i = 0

while i < amount:
    i += 1
    init += val

print("the sum of series is :",init)

# I Actually thought it would be nicer not to use loops here,
# and for example use the formula:
# https://he.wikipedia.org/wiki/%D7%A1%D7%93%D7%A8%D7%94_%D7%97%D7%A9%D7%91%D7%95%D7%A0%D7%99%D7%AA
# But your solution is also cool
