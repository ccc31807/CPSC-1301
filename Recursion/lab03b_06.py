# lab03b_06.py

import sys

if len(sys.argv) != 3:
    print("Call this method with two integer parameters: <dividend>, <divisor>")
    sys.exit()

dividend = int(sys.argv[1])
divisor = int(sys.argv[2])
quotient = 0

print("calling divide( %d, %d, %d)" % (quotient, dividend, divisor))
def divide(quotient, dend, dsor):
    if dend < dsor:
        print("The quotient is", quotient, "and the remainder is", dend)
    else:
        divide(quotient + 1, dend - dsor, dsor)


divide(quotient, dividend, divisor)
