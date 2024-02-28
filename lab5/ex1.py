#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re
pattern = re.compile('ab*')

string = input("Write your text: ")

m = pattern.search(string)

if m:
    print('Match found:', m.group())
else:
    print('No match')
