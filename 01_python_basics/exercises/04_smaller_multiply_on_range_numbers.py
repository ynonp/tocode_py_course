#!/usr/bin/env python3

from random import randint
from math import gcd

num_a = randint(1,10)
num_b = randint(1,10)

print(f"{num_a} and {num_b}, give {gcd(num_a,num_b)}")



