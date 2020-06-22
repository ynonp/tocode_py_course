#!/usr/bin/env pyhton3
import time
import getpass


db = {
        "apple"   : "red",
        "lettuce" : "green",
        "lemon"   : "yellow",
        "orange"  : "orange",
        }

def check_login(name, passwd):
    try:
        print("Connecting to DB or login check, Please Wait")
        # Cool :)
        # time.sleep(2)
        # No need to use .keys() here, if name in dict is good
        # But I would use try try/except block
        # Also note you had a typo there and so always ended up in the
        # except block
        if db[name] == passwd:
            print("Welcome Master")
    except:
        print("Go Away Intruder")


if __name__ == "__main__":
    n = input("Please Provide Login Name: ")
    # Cool!
    p = getpass.getpass("Please Provide Login Password: ")

    check_login(n,p)





