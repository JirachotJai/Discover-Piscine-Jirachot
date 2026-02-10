#!/usr/bin/python3

num = (input("Give me a number : "))

try:
    num = int(num)
    print("The number is an Integer")
except ValueError:
    try:
        num = float(num)
        print("The number is an decimal.")
    except ValueError:
        print("")
