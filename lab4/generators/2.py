def get_even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


numbers = get_even_numbers(10)
print(*numbers, sep=", ")

