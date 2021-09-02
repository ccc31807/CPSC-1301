# lab03b_05.py

import sys

if len(sys.argv) != 2:
    print("Call this method with one integer parameter")
    sys.exit()

numBeers = int(sys.argv[1])

def drink(nb):
    if nb == 0:
        print("All gone, burp ...")
    else:
        print(nb, "beers left")
        drink(nb - 1)

drink(numBeers)

