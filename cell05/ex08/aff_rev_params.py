#!/usr/bin/python3
import sys

if len(sys.argv) - 1 <= 1:
    print("none")
else:
    for arg in reversed(sys.argv):
        if arg == sys.argv[0]:
            break
        print(arg, end ="\n")