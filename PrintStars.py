# Prints a line containing the specificied
# number of stars. Assume that n >= 0

def printStars(n):
    for i in range(n):
        print("*",end="")
    print()

def printStarsRecursive(n):
    if n == 0:
        print()
    else:
        print("*",end="")
        printStarsRecursive(n-1)

printStars(10)
printStarsRecursive(10)