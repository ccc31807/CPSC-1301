#!python

# Name recur02.py
# Author: Charles Carter
# Date: May 17, 2021
# Purpose: to return a string of characters

#import pdb
#breakpoint()

import string

list02 = "hello"

def sum01(s, l):
    if len(l) == 0:
        return s
    else:
        return sum01(s + l[0].upper(), l[1:])

if __name__ == '__main__':
   sum = sum01("", list02) 
   print('string is ', sum)
