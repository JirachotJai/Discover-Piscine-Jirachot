#!/usr/bin/python3

txt = input()
result = ""

for i in txt:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()
    else:
        result += i

print(result)