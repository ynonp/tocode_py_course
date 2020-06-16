#!/usr/bin/env python3
import sys
from random import randint

while True:
    num = randint(1,1000000)
    if (num % 7 == 0)  and (num %13 == 0) and (num % 15 == 0):
        print(num)
        # I prefet never to use sys.exit()
        # (or rather rarely)
        # because sys.exit() will skip code that may appear later
        # also it's worth noting that you usually want to provide a parameter to
        # sys.exit() for example:
        # sys.exit(1) - marks this program as failed
        # sys.exit(0) - marks this program as succeeded
        # sys.exit("Error reading file") - prints to stderr AND marks program as failed
        sys.exit()
    else:
        continue

# A nicer alternative IMHO would be to use continue
while True:
    num = randint(1, 1_000_000)
    if num % 7 != 0:  continue
    if num % 13 != 0: continue
    if num % 15 != 0: continue

    # We're here - so all 3 conditions didn't happen
    break

print(num)
