#EXERCISE.1

def function_to_convert(your_grams):
    ounces = float(your_grams) * 28.3495231
    return ounces
    
def main():
    your_grams = input("Enter the weight in grams: ")
    converted_result = function_to_convert(your_grams)
    print("Result of conversion:", converted_result)

if __name__ == "__main__":
    main()


#EXERCISE.2

def converting_to_centigrade(temperature):
    centigrade = (5 / 9) * (temperature - 32)
    return centigrade

def main():
    temperature_in_F = int(input("Fahrenheit: "))
    result = converting_to_centigrade(temperature_in_F)
    print("The equivalent Centigrade temperature: ", result)

if __name__ == "__main__":
    main()



#EXERCISE.3

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None

def main():
    num_heads = int(input("Enter the number of heads: "))
    num_legs = int(input("Enter the number of legs: "))

    result = solve(num_heads, num_legs)
    if result:
        chickens, rabbits = result
        print("Number of chickens:", chickens)
        print("Number of rabbits:", rabbits)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()


# #EXERCISE.4
# #You are given list of numbers separated by spaces. 
# #Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

# def filter_prime(n): 
#     if n <= 0: 
#         return False
#     elif n == 1: 
#         return False
#     for i in range(2, int(n ** 0.5) + 1): 
#         if n % i == 0: 
#             return False
#     return True

# # #EXERCISE.5
# # #Write a function that accepts string from user and print all permutations of that string.

# def permute_string (string, answer):
    
#     for i in range(len(string)):
#         ch = string[i]
#         left_substr = string[0:i]
#         right_substr = string[i + 1:]
#         rest = left_substr + right_substr
#         permute_string(rest, answer + ch)

# # #EXERCISE.6
# # #Write a function that accepts string from user, return a sentence with the words reversed.

# def reverse(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str
    
# # #EXERCISE.7
# # #Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# def has_33(numbs):
#     i = 0
#     while i < len(numbs)-1:
#         if numbs[i] == 3:
#             if numbs[i+1] == 3:
#                 return True
#         i += 1
#     return False

# numbers = input()
# numbs = numbers.split()
# numbs = [int(num) for num in numbs]
# print(has_33(numbs))

# if __name__ == "__main__":
#     main()


# # #EXERCISE.8
# # #Write a function that takes in a list of integers and returns True if it contains 007 in order

# def spy_game(numbs):
#     s = ''
#     for i in numbs:
#         s += i
#     if '007' in s:
#         return True
#     return False

# numbers = input()
# numbs = numbers.split()
# print(spy_game(numbs))

# if __name__ == "__main__":
#     main()

# # #EXERCISE.9
# # #Write a function that computes the volume of a sphere given its radius.

# def volume_of_sphere(radius):
#     v_sphere = 4/3*3.14*radius**3
#     return v_sphere 

# def main():
#     radius = int(input("Enter the radius: "))
#     result = volume_of_sphere(radius)
#     print("The volume of a sphere is:", result)

# if __name__ == "__main__":
#     main()

# # #EXERCISE.10

# def unique_elements(l):
#     new_list = []
#     i = 0
#     while i < len(l):
#         t_or_f = True
#         j = 0
#         while j < i:
#             if l[i] == l[j]:
#                 t_or_f = False
#             j += 1
#         if t_or_f:
#             new_list.append(l[i])
#         i += 1
#     return new_list

# l = input()
# elements = l.split()
# new_list = unique_elements(elements)
# print(new_list)

# if __name__ == "__main__":
#     main()

# # #EXERCISE.11

# def palindrome(text):
#     i = 0
#     j = len(text)-1
#     while i < len(text)/2:
#         if text[i] != text[j]:
#             return 'No palindrome'
#         i+=1
#         j-=1
#     return 'palindrome'

# text = input()
# print(palindrome(text))

# if __name__ == "__main__":
#     main()

# # #EXERCISE.12
# def histogram(gist):
#     i = 0
#     while i < len(gist):
#         j = 0
#         while j < gist[i]:
#             print('*', end='')
#             j += 1
#         print()
#         i += 1

# gist = input()
# gist = gist.split()
# gist = [int(num) for num in gist]
# histogram(gist)
# if __name__ == "__main__":
#     main()

# # #EXERCISE.13
# import random

# def find_num_random(rand_num, count):
#     count += 1
#     num = int(input('Take a guess.\n'))
#     if num == rand_num:
#         print(f'Good job, KBTU! You guessed my number in {count} guesses!')
#         return
#     print('\nYour guess is too low.')
#     return find_num_random(rand_num, count)

# name = input('Hello! What is your name?\n')
# number = random.randint(1, 20)
# count = 0
# print(f'Well, {name}, I am thinking of a number between 1 and 20.\n')
# find_num_random(number, count)

# if __name__ == "__main__":
#     main()
