#Write a Python program to insert spaces between words starting with capital letters.

import re

def insert_spaces(text):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return result

text = input()
result = insert_spaces(text)
print(result)
