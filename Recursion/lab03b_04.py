# lab03b_04.py

import sys

if len(sys.argv) != 2:
    print("INCORRECT. Call with one integer parameter.")
    sys.exit()

top = int(sys.argv[1])
print("I'm adding to", top)

def myFun(sum, n):
    if n > top:
        print("The sum is", sum)
    else:
        myFun(sum + n, n + 1)

myFun(0, 0)
