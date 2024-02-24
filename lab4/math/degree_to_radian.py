#1 method

import math
your_degree = int(input("Input degree: "))
result = math.radians(your_degree)
print("Output radian:", round(result,7))

#2 method
import math
def converting(degree):
    radians = degree * (math.pi/180)
    return radians

def main():
    degree = int(input("Input degree: "))
    result = converting(degree)
    print("Output radian: ", result)

if __name__ == "__main__":
    main()

