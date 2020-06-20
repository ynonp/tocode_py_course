#!/usr/bin/env pyhton3
import time
import getpass 

db = {"apple":"red", "lettuce":"green", "lemon":'yellow', "orange":"orange"}

def check_login(name, passwd):
    try:
        print("Connecting to DB or login check, Please Wait")
        time.sleep(2)
        if name in db.keys() and passwd == db[name]:
            print("Welcome Master")
        else:
            print("Intruder Alert")
    except:
        print("Some error occured, please try to debug")


if __name__ == "__main__":
    n = input("Please Provide Login Name: ")
    p = getpass.getpass("Please Provide Login Password: ")

    check_login(n,p)





