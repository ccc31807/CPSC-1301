#!python
# Name: MathGames.py
# Author: Charles Carter
# Date; May 16, 2021
# Purpose: Math Games, addition, subtraction, multiplication, division

import random
import math
from os import system

def hello():
    print("Hello from 'MathGames.py'")

def showMenu():
    print("Welcome to Math  Games\nPlease choose your test:")
    while True:
        choice = interface()
        if choice == 1:
            grade = add(numques())
            print("You made a ", grade)
        elif choice == 2:
            grade = sub(numques())
            print("You made a ", grade)
        elif choice == 3:
            grade = mul(numques())
            print("You made a ", grade)
        elif choice == 4:
            grade = div(numques())
            print("You made a ", grade)
        elif choice == 9:
            break
        else:
            print("Sorry, I don't understand")
    print("Goodbye")

def interface():
    s = """
1. Addition
2. Subtraction
3. Multiplication
4. Division
9. Exit
        """
    choice = int(input(s))
    return choice

def numques():
    n = int(input("How many questions to you want to answer? "))
    top = int(input("Enter the range of the test from 0 to ? "))
    return (n, top)


def get_rand_nums(top):
    lhs = random.randint(0, top)
    rhs = random.randint(0, top)
    return (lhs, rhs)

def add(ntup):
    system("cls")
    print("Addition")
    n, top = ntup
    correct = 0
    for i in range(1, n+1):
        lhs, rhs = get_rand_nums(top)
        print("{0}. What is {1} + {2}? ".format(i, lhs, rhs))
        answer = int(input())
        if answer == (lhs + rhs):
            print("Correct")
            correct += 1
        else:
            print("Incorrect, the answer is", lhs + rhs)
    return float(100 * correct / n)

def sub(ntup):
    system("cls")
    print("Subtraction")
    n, top = ntup
    correct = 0
    for i in range(1, n+1):
        lhs, rhs = get_rand_nums(top)
        if lhs < rhs:
            lhs, rhs = rhs, lhs
        print("{0}. What is {1} - {2}? ".format(i, lhs, rhs))
        answer = int(input())
        if answer == (lhs - rhs):
            print("Correct")
            correct += 1
        else:
            print("Incorrect, the answer is", lhs - rhs)
    return float(100 * correct / n)

def mul(ntup):
    system("cls")
    print("Multiplication")
    n, top = ntup
    correct = 0
    for i in range(1, n+1):
        lhs, rhs = get_rand_nums(top)
        print("{0}. What is {1} * {2}? ".format(i, lhs, rhs))
        answer = int(input())
        if answer == (lhs * rhs):
            print("Correct")
            correct += 1
        else:
            print("Incorrect, the answer is", lhs * rhs)
    return float(100 * correct / n)

def div(ntup):
    system("cls")
    print("Division")
    tolorance = 0.05
    n, top = ntup
    correct = 0
    for i in range(1, n+1):
        lhs, rhs = get_rand_nums(top)
        if rhs == 0:
            lhs, rhs = get_rand_nums(top)
        print("{0}. What is {1} / {2}? ".format(i, lhs, rhs))
        answer = float(input())
        if abs(answer - (lhs / rhs)) < tolorance:
            print("Correct")
            correct += 1
        else:
            print("Incorrect, the answer is", lhs / rhs)
    return float(100 * correct / n)

#main function executes the defined functions
if __name__ ==  '__main__':
    hello()
    showMenu()





