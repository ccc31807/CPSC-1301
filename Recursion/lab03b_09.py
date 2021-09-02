# recur00a.py

groceries = ["milk","bread","diapers","chips","salsa"]

def printlist(g):
    print("Here is my list")
    print(g)
    print("--------------------")

def shop(g):
    if len(g) == 0:
        print("headed to checkout ...")
    else:
        print(g[0], "in cart")
        shop(g[1:])

printlist(groceries)
shop(groceries)

