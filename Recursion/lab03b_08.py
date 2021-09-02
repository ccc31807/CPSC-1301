#!python

# Name lab03b_08.py
# Author: Charles Carter
# Date: May 17, 2021
# Purpose: to add all integers between <start> and <end>

def addem(total, start, end):
    if start > end:
        print("The total is", total)
    else:
        addem(total + start, start + 1, end)

print("Enter the starting integer: ", end = '')
start = int(input())
print("Enter the ending integer: ", end = '')
end = int(input())
print("start is", start, " and end is", end)

addem(0, start, end)

