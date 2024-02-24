def area_paralell(length, height):
    area = length * height
    return area
def main():
    length = int(input("Length of base: "))
    height = int(input("Height of parallelogram: "))
    
    result = float(area_paralell(length, height))
    
    print("Area of a parallelogram:",result)
    
if __name__ == "__main__":
    main()