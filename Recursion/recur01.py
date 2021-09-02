#!python

# Name recur01.py
# Author: Charles Carter
# Date: May 17, 2021
# Purpose: to return the sum of a list of integers

#import pdb
#breakpoint()

list01 = [1,2,3,4,5]

#def sum01(s, l):
#    print('sum01(', s, ',', l, ')')
#    if len(l) == 0:
#        print('\tif:', s)
#        return s
#    else:
#        s += l[0]
#        print('\telse:', s)
#        return sum01(s, l[1:])

def sum01(s, l):
    if len(l) == 0:
        return s
    else:
        return sum01(s + l[0], l[1:])

if __name__ == '__main__':
   sum = sum01(0, list01) 
   print('total is ', sum)
