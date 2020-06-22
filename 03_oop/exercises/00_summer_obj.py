#!/usr/bin/env python3

class Summer:
    def __init__(self):
        self.total = 0
    
    def add(self,*args):
        for i  in args:
            self.total = self.total + i 
        return self.total

    def print_total(self):
        print(f"{self.total}")


s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
s.print_total()

# should print 50
t.print_total()
