#!/usr/bin/env python3

# You don't need a list here, a simple integer will work just fine
max_value = float('-inf')
numbers_read = 0
while numbers_read < 10:
    i = int(input(f"{numbers_read}) enter a num: "))
    if i > max_value:
        max_value = i

print(f"the biggest num would be {max_value}")
