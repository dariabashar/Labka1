def trapezoid(height, base1, base2):
    result = ((base1+base2)*height)*0.5
    return result

def main():
    height = int(input("Height: "))
    base1 = int(input("Base, first value: "))
    base2 = int(input("Base, second value: "))
    
    result = trapezoid(height, base1, base2)
    print("Area of a trapezoiid: ", result)
    
if __name__ == "__main__":
    main()