#!/usr/bin/env python3
import sys
from random import randint

while True:
    num = randint(1,1000000)
    if (num % 7 == 0)  and (num %13 == 0) and (num % 15 == 0):
        print(num)
        sys.exit()
    else:
        continue


