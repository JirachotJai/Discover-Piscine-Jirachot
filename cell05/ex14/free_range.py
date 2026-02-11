#!/usr/bin/python3
import sys

result = "none"

if len(sys.argv) - 1 == 2:
    result = list(range(int(sys.argv[1]), int(sys.argv[2])+1))

print(result)