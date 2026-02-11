#!/usr/bin/python3

first_arr = [2, 8, 9, 48, 8, 22, -12, 2]
temp = set(first_arr)
result = []

for num in temp:
    if num > 5:
        result.append(num+2)

result = set(result)

print(f"{first_arr}\n{result}")