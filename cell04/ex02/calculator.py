#!/usr/bin/python3
import operator
first_num = int(input("Give me the first number: "))
sec_num = int(input("Give me the second number: "))

print("Thank you!")

for i in range (4):
    if i == 1:
        print(f"{first_num} - {sec_num} = {first_num-sec_num}")
    elif i == 2:
        print(f"{first_num} / {sec_num} = {round(first_num/sec_num, 2)}")
    elif i == 3:
        print(f"{first_num} * {sec_num} = {first_num*sec_num}")
    else:
        print(f"{first_num} + {sec_num} = {first_num+sec_num}")