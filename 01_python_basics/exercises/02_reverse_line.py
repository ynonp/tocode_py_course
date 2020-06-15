#!/usr/bin/env python3

import os

data = ""

while True:
    try:
        data = input()
        print(data[::-1])
    except ValueError:
        print("Data missing")
