#!/usr/bin/env python3

age = 0

while age == 0 or age < 0: 
    age = int(input("please provide your age: "))

print("your age in month would be :", age * 12)