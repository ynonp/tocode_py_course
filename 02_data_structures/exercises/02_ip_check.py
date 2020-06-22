#!/usr/bin/env python3

###################################################
#created by :   Pushtakio
#purpose    :   
#date       :
#version    :   0.0.1
###################################################

import sys

user_list= sys.argv[1:]

# Using dict comprehension makes this code much cleaner
def convert_file_data_dict(val):
    splitstrs = [s.strip().split('=') for s in val]
    return {
            host: ip_address for host, ip_address in splitstrs
            }

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


