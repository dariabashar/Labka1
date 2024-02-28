#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

pattern = re.compile('[a-z]+_[a-z]+')

string = input("Write your text: ")

m = pattern.findall(string)

if m:
    print('Match found:', m)
else:
    print('No match')