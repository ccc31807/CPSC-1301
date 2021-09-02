#!python

# Name lab03b_07.py
# Author: Charles Carter
# Date: May 17, 2021
# Purpose: to return a string of characters

import string

myString = "hello world"

def recur_str(s, l):
    if len(l) == 0:
        return s
    else:
        return recur_str(s + l[0].upper(), l[1:])

if __name__ == '__main__':
   sum = recur_str("", myString) 
   print('string is ', sum)
