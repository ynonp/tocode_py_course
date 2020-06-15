#!/usr/bin/env python3


age = input("Please enter your age: ")
while not age.isnumeric():
    age = input("Please enter your age: ")

print(int(age)*12)
