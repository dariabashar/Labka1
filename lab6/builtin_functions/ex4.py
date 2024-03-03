import time

def square_root(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = pow(number, 0.5)
    return result

def main():
    number = int(input("Enter a number: "))
    milliseconds = int(input("Enter milliseconds: "))
    result = square_root (number, milliseconds)
    print ( "Square root of", number,  "after", milliseconds, "milliseconds is", result )

if __name__ == "__main__":
    main()
