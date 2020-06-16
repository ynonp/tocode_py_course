#!/usr/bin/env python3


age = input("Please enter your age: ")
# Please review the example in this lesson:
# https://www.tocode.co.il/bundles/python/lessons/10-exceptions?tab=video
# As to how to write this loop
# (The problem with checking isnumeric is that it returns the wrong answers,
#  for example '2.4'.isnumeric() is false)
while not age.isnumeric():
    age = input("Please enter your age: ")

print(int(age)*12)
