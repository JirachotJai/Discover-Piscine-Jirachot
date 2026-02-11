#!/usr/bin/python3
import sys

if len(sys.argv) - 1 >= 1:
    for txt in sys.argv[1:]:  
        if not txt.endswith("ism"):
            print(txt+"ism")
else:
    print("none")



    