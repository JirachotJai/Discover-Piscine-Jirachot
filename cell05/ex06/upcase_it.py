#!/usr/bin/python3
import sys

if len(sys.argv) - 1 != 1:
    print("none")
else:
    for i in sys.argv[1:]:
        print(i.upper())