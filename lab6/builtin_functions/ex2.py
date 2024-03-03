#Write a Python program with builtin function that accepts a string and 
#calculate the number of upper case letters and lower case letters

def main():
    string = input("Write your string: ")
    upper_count = sum(1 for c in string if c.isupper())
    lower_count = sum(1 for c in string if c.islower())
    print("Lowercase:", lower_count)
    print("Uppercase:", upper_count)

if __name__ == "__main__":
    main()
