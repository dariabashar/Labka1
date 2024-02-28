#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

pattern = re.compile('ab{2,3}')

string = input("Write your text: ")

m = pattern.search(string)

if m:
    print('Match found:', m.group())
else:
    print('No match')