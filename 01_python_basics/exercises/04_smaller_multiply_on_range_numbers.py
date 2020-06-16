#!/usr/bin/env python3

from random import randint
from math import gcd

num_a = randint(1,10)
num_b = randint(1,10)

# Actually the goal here was to calculate lowest common multiplication of the numbers
# https://he.wikipedia.org/wiki/%D7%9B%D7%A4%D7%95%D7%9C%D7%94_%D7%9E%D7%A9%D7%95%D7%AA%D7%A4%D7%AA_%D7%9E%D7%99%D7%A0%D7%99%D7%9E%D7%9C%D7%99%D7%AA
print(f"{num_a} and {num_b}, give {gcd(num_a,num_b)}")



