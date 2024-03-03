#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def palindrom_or_not (string):
    rev = ''.join(reversed(string))
    return string == rev
    
def main():
    string = input()
    result = palindrom_or_not(string)
    
    print(result)
    
if __name__ == "__main__":
    main()
    