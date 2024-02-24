import math 
def area_polygon(num, length):
    area = num * (length ** 2) / (4 * math.tan(math.pi / num))
    return area

def main():
    number_of_slides = int(input("Input number of sides: "))
    length = int(input("Input the length of a side: "))
    
    result = int(area_polygon(number_of_slides,length))
    print("The area of the polygon: ",result)
    
if __name__ == "__main__":
    main()