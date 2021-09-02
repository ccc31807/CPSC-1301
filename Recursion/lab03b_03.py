# lab03b_03.py

import sys

if len(sys.argv) != 2:
    print("INCORRECT. Call with one integer parameter.")
    sys.exit()

top = int(sys.argv[1])
print("I'm counting to", top)

def myFun(n):
    if n > top:
        print("Done!")
    else:
        print(n)
        myFun(n + 1)

myFun(1)
