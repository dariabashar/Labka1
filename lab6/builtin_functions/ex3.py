#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

my_input_string = input()
reversed_string = ''.join(reversed(my_input_string))
print(my_input_string == reversed_string)
