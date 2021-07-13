#! python
# Name: FirstProgram.py
# Author: Charles Carter
# Date: July 13, 2021
# Purpose: to illustrate how to write a progra in Python

# import statements go here

# user defined functions go here
def plainHello():
    print("Hello from plainHello()")

def helloWithArg(arg):
    print("Hello", arg, "from helloWithArg(name)")

def sumReturnVal():
    lhs = 4
    rhs = 5
    sum = lhs + rhs
    #return("The sum of", lhs, "and", rhs, "is", sum)
    rv = "The sum of " + str(lhs) + " and " + str(rhs) + " is " + str(sum)
    return(rv)

def sumWithArgAndRet(lhs, rhs):
    return("The sum of " + str(lhs) + " and " + str(rhs) + " is " + str(lhs + rhs))


# this is the "main" function
if __name__ == "__main__":
    print("Hello from main")
    plainHello()
    name = "Charles"
    helloWithArg(name)

    rv = sumReturnVal()
    print(rv)

    rv = sumWithArgAndRet(6, 7)
    print(rv)
    print(sumWithArgAndRet(24, 27))
