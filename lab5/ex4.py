#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

pattern = re.compile('[A-Z][a-z]+')

string = input("Write your text: ")

m = pattern.findall(string)

if m:
    print('Match found:', m)
else:
    print('No match')