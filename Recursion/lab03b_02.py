# lab03b_02.py

def funcA():
    print("calling funcB()")
    funcB()

def funcB():
    print("calling funcC()")
    funcC()

def funcC():
    print("This is function C")

funcA()
