#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re


def replace_with_colon(text1):
    # result = text1.replace(' ', ':').replace(',', ':').replace('.', ':')
    
    return re.sub(r'[ ,.]', ':', text)


text = input("Write your text: ")

print(replace_with_colon(text))