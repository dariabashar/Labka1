number = int(input())


def generate_squares(upper_bound):
    for i in range(1, upper_bound + 1):
        yield i ** 2


squares_generator = generate_squares(upper_bound=number)
for square in squares_generator:
    print(square)

