#!python
# Name: Hello.py
# Author: Charles Carter
# Date; May 19, 2021
# Purpose: programming exercise 01: writing and calling methods that take no parameters and return no values

import sys
import platform

def hello():
    print("This is programming exercise 01, Hello")
    print()

def helloname():
    print("Hello from Charles Carter")
    print()

def sys_info():
    print("version:", sys.version)
    print("version_info:", sys.version_info)
    print()
    
def platform_info():
    print("system:", platform.system())
    print("node:", platform.node())
    print("release:", platform.release())
    print("version:", platform.version())
    print("machine:", platform.machine())
    print("processor:", platform.processor())
    print("platform:", platform.platform())
    print()

def print_csu():
    print("CCCCCCCC   SSSSSSSS   UU    UU")
    print("CCCCCCCC   SSSSSSSS   UU    UU")
    print("CC         SS         UU    UU")
    print("CC         SS         UU    UU")
    print("CC         SSSSSSS    UU    UU")
    print("CC         SSSSSSS    UU    UU")
    print("CC              SS    UU    UU")
    print("CC              SS    UU    UU")
    print("CCCCCCCC   SSSSSSSS   UUUUUUUU")
    print("CCCCCCCC   SSSSSSSS   UUUUUUUU")
    print()

#main function executes the defined functions
if __name__ ==  '__main__':
    hello()
    helloname()
    sys_info()
    platform_info()
    print_csu()
