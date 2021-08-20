#! python
# Name: lab01b_carter.python
# Author: Charles Carter
# Date: August 19, 2021
# Purpose: to demonstrate a Python program


#import modules


#user defined functions
def hello_fun():
    print("hello from function")

def input_fun(name):
    print("Greetings", name)
    
def output_fun():
    return "Hello from output_fun"
    
def add():
    print("Enter the lefthand side:", end = "")
    lhs = int(input())
    print("Enter the righthand side:", end = "")
    rhs = int(input())
    sum = lhs + rhs
    return sum

#main functions
if __name__ == "__main__":
    print("Hello from main")
    hello_fun()
    moniker = "Charles"
    input_fun(moniker)
    var1 = output_fun()
    print(var1)
    
    print("Enter your name: ", end = "")#prompt
    name = input()
    input_fun(name)
    
    s = add()
    print("The sum is", s)
    
    
    
    
    

