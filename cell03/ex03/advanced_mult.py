#!/usr/bin/python3
import sys

temp = ""
row = 0
mult_num =0

if len(sys.argv) > 1:
    print("none")
    sys.exit()

while row < 11:
    while mult_num < 11:
        temp += str(mult_num*row)+" "
        mult_num += 1
    print(f"Table de {row}: {temp}")
    temp = ""
    mult_num = 0
    row += 1
        