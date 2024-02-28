#Write a Python program to convert a given camel case string to snake case.

import re


def camel_to_snake(match):
    return match.group(1) + "_" + match.group(2).lower()


def convert_camel_to_snake(snake_str):
    camel_str = re.sub(r'([a-z])([A-Z])', camel_to_snake, snake_str)
    return camel_str


camel_case_string = input()
snake_case_string = convert_camel_to_snake(camel_case_string)
print(snake_case_string)