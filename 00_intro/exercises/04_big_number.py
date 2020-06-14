#!/usr/bin/env python3

tmp_max = 0

print("Please enter 3 numbers: ")
n1 = int(input())
n2 = int(input())
n3 = int(input())


if n1 > tmp_max:
    tmp_max = n1

if n2 > tmp_max:
    tmp_max = n2

if n3 > tmp_max:
    tmp_max = n3

print("the biggest number is :", tmp_max)

# So, python has a max() function
print(max(n1, n2, n3))


