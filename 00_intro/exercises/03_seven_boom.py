#!/usr/bin/env python3


num = int(input("Please provide number: "))

if num / 7 == 1 or num % 7 == 0:
     print("Boom, bring out the pain")
# Why not use just a string?
elif "7" in str(num):
    print("Boom Bada Bim")
else:
    print("ahhh what a wonderful number",num)
