#Write a python program to convert snake case string to camel case string.

import re

def match_to_upper(match):
    return match.group(1).upper()

def convert_snake_to_camel(snake_str):
    camel_str = re.sub(r'_([a-zA-Z])', match_to_upper, snake_str)
    return camel_str


snake_case_string = input()
camel_case_string = convert_snake_to_camel(snake_case_string)
print(camel_case_string)