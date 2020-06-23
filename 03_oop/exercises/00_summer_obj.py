#!/usr/bin/env python3

class Summer:
    def __init__(self):
        # Better to use _ before a private member name
        # (It's a convention but useful one)
        self._total = 0
    
    def add(self,*args):
        # Python already has a sum function
        self._total += sum(args)
        # And I deleted your "return" statement because
        # nobody looks on the return value

    def print_total(self):
        # Since you only have one variable, no need to use format string here
        print(self._total)


s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
s.print_total()

# should print 50
t.print_total()
