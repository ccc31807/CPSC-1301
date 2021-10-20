#!python
# Name: ListPlay.py
# Author: Charles Carter
# Date; May 23, 2021
# Purpose: while and for loops

def hello():
    print("Hello from 'ListPlay.py'")


def print_list(li):
    for i in range(len(li)):
        print(li[i], ' ', end='')
    print()


def print_list_reversed(li):
    length = len(li)
    for i in range(length):
        print(li[(length - 1) - i], end = ' ')
    print()

def print_list_rotated(li, direction, place):
    length = len(li)
    if direction == 'R' or direction == 'r':
        place = length - place
    for i in range(length):
        print(li[(i + place) % length], end=' ')
    print()

def print_bubble_sort(li):
    length = len(li)
    for i in range(0,length-1):
        for j in range(i,length):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    print_list(li)

#main function executes the defined functions
if __name__ ==  '__main__':
    hello()

    x1 = [0,2,4,6,8]
    x2 = [1,3,5,7,9]
    x3 = [3,1,4,1,5,9,2,6,5,3,5]
    x4 = "abcdefghij"
    x5 = "Your Name"

    print("printing the lists")
    print_list(x1)
    print_list(x2)
    print_list(x3)
    print_list(x4)
    print_list(x5)

    print("printing the lists in reverse order")
    print_list_reversed(x1)
    print_list_reversed(x2)
    print_list_reversed(x3)
    print_list_reversed(x4)
    print_list_reversed(x5)

    print("printing the rotated lists")
    print_list_rotated(x1, "L", 2)
    print_list_rotated(x2, "R", 3)
    print_list_rotated(x3, "L", 4)
    print_list_rotated(x4, "R", 5)
    print_list_rotated(x5, "L", 6)

    print("printing the sorted list")
    print_bubble_sort(x3)
    print_bubble_sort(list(x5))

