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
    sum_num = 0 
    for i in num:
        sum_num = sum_num + int(i)

    avg = sum_num / len(num)
    return avg

if __name__ == "__main__":
#    try:
    if len(data) <= 0 or len(data) >20:
        os.system("clear")
        time.sleep(1)
        print("the data is corrupted")
    else:
        avg_num = calc_avg(data)
        new_data = []
        for i in data:
            if int(i) >= avg_num:
                new_data.append(i)
            else:
                pass

    print(f"the new grade list is {new_data} and average is {avg_num}")
#    except:
#        print("Exception error")
