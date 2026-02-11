#!/usr/bin/python3
import sys
result = ""

def downcase_it(txt : str):
    return txt.lower()

if len(sys.argv) - 1 == 0:
    print("none")
else:
    for arg in sys.argv[1:]:
        print(downcase_it(arg))

