#!/usr/bin/env python3

class MyCounter():
    count = 0

    # Great!
    def __init__(self):
        MyCounter.count += 1





for _ in range(10):
     c1 = MyCounter()

# should print 10
print(MyCounter.count)
