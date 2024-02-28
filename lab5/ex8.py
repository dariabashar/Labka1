#Write a Python program to split a string at uppercase letters.

import re

def split_at_uppercase(string):
    parts = re.findall('[A-Z][^A-Z]*', string)
    return parts

string = input()
result = split_at_uppercase(string)
print(result)
