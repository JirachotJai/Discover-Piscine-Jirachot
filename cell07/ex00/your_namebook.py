#!/usr/bin/python3
import sys

persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindcier"
    }

def array_of_names(name : dict):
    result = []
    for txt in name:
        result.append(f"{txt.capitalize()} {name.get(txt).capitalize()}")
    return result

print(array_of_names(persons))
