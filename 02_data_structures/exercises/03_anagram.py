#!/usr/bin/env python3

###################################################
#created by :   Pushtakio
#purpose    :   
#date       :
#version    :   0.0.1
###################################################

import os.path
import time
import sys

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  
user_input = sys.argv[1:]

if len(user_input) <= 0:
    print("please provide full path")
    time.sleep(2)
    clear()
    sys.exit(1)


