#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

pattern = re.compile('a.*b$')

string = input("Write your text: ")

m = pattern.match(string)

if m:
    print('Match found:', m.group())
else:
    print('No match')