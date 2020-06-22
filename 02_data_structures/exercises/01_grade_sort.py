#!/usr/bin/env python3

###################################################
#created by :   Pushtakio
#purpose    :   
#date       :
#version    :   0.0.1
###################################################

import os
import sys
import time

data = sys.argv[1:]

def calc_avg(num):
    # Average is just sum() / len()
    return sum(num) / len(num)

if __name__ == "__main__":
#    try:
    if len(data) <= 0 or len(data) > 20:
        os.system("clear")
        time.sleep(1)
        # Assume we're here - so our next line is the final print
        # statement. But that's not the right flow, because if data is corrupted
        # you don't want to print the average
        # This is exactly the case for exceptions:
        raise Exception("the data is corrupted")

    avg_num = calc_avg(data)
    # Please watch the lists video here, specifically the part on List Comprehension:
    # https://www.tocode.co.il/bundles/python/lessons/12-lists
    new_data = [i for i in data if int(i) >= avg_num]

    print(f"the new grade list is {new_data} and average is {avg_num}")
#    except:
#        print("Exception error")
