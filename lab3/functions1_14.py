#EXERCISE.14
from functions1_1to13 import function_to_convert, solve, converting_to_centigrade


your_grams = input("Enter the weight in grams: ")
converted_result = function_to_convert(your_grams)
print("Result of conversion:", converted_result)


num_heads = int(input('Enter number of heads: '))
num_legs = int(input('Enter number of legs: '))
chickens,rabbits  = solve(num_heads, num_legs)
print("The number of chickens is: ", chickens)
print("The number of rabbits is: ", rabbits)


temperature_in_F = int(input("Fahrenheit: "))
result = converting_to_centigrade(temperature_in_F)
print("The equivalent Centigrade temperature: ", result)
