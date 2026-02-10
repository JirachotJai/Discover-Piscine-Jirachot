#!/usr/bin/python3
first_num = int(input("Enter the first number: \n"))
sec_num = int(input("Enter the second number: \n"))

value = first_num * sec_num

if value > 0:
    result = "positive"
elif value < 0:
    result = "negative"
else:
    result = "positive and negative"

print(f"{first_num} x {sec_num} = {value}\nThe result is {result}")