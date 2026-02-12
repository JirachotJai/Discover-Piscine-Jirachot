#!/usr/bin/python3
import sys


if len(sys.argv) - 1 >= 1:
    print(f"parameters: {len(sys.argv)}")
    for txt in sys.argv[1:]:
        print(f"{txt}: {len(txt)}")
else:
    print("none")


    