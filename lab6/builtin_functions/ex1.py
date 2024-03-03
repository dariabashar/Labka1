from functools import reduce

def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)

list1 = input("Write numbers for list: ")

numbers = list1.split()

numbers = list(map(int, numbers))

print("Result: ", multiply(numbers))

