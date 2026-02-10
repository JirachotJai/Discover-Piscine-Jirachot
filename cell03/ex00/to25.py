#!/usr/bin/python3
number = int(input('Enter a number less than 25 :'))

if number > 25:
    print("Error")
else:
    for n in range(number, 26):
        print("Inside the loop, my variable is %d" %n)