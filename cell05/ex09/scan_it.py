#!/usr/bin/python3
import sys
import re
result = "none"

if len(sys.argv) - 1 == 2:
    search = sys.argv[1]
    target = sys.argv[2]

    if len(re.findall(search, target)) != 0:
        result = len(re.findall(search, target))



print(result)
    