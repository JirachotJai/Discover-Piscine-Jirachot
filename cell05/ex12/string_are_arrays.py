#!/usr/bin/python3
import sys

result = "none"

if len(sys.argv) - 1 == 1:
    result = ""
    for txt in sys.argv[1]:
        
        if txt == "z":
            result += txt

print(result)


    