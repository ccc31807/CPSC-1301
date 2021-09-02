# lab03b_10.py


def build(what):
    print("Please enter a character or digit, <RETURN> to finish: ", end = '')
    char = input()
    if char == "":
        print(what)
    else:
        build(what + char)

build("")

