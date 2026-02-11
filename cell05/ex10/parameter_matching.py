#!/usr/bin/python3
import sys

result = "none"

if len(sys.argv) - 1 == 1:
    guess = input("What was the parameter? ")

    if sys.argv[1] == guess:
        result = "Good job!"
    else:
        result = "Nope, sorry..."


print(result)
    