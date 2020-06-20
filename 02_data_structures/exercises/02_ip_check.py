#!/usr/bin/env python3

###################################################
#created by :   Pushtakio
#purpose    :   
#date       :
#version    :   0.0.1
###################################################

import sys

user_list= sys.argv[1:]

def convert_file_data_dict(val):
    db={}
    for v in val:
        tmp = v.split('=')
        db[tmp[0]]=tmp[1]

    return db

with open('addr.txt') as addr:
    addresses = addr.readlines()
    addr_dict = convert_file_data_dict(addresses)


if __name__ == "__main__":
#    if len(user_list) == 0:
#        print("host names not provided")
#        sys.exit(1)
#    else:
    try:
        for i in user_list:
            print(f"{i}==>>{addr_dict[i]}")
    except KeyError:
        print("No such hostname")
    except:
        print("Undefying error occured")


