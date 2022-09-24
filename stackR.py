import stackLib as sl
# import csv

sl.clearData()
while True:
    userInput = input("Choose action:\n 1. Add block to stack\n 2. Compute Stackup\n")
    if userInput == "2": break
    while True:
        dim = input("Enter block dimension: ")
        if dim == "": break
        tol = input("Enter block symmetric tolerance: ")
        sign = input("Enter 1 or -1 for block direction: ")
        sl.writeBlock(dim, tol, sign)

stackup = sl.readData()

print("Stackup gap: " + str(stackup.stackup))
print("Maximum stackup range: " + str(stackup.tol))
print("RSS stackup range: " + str(stackup.rssTol))