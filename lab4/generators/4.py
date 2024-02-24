
def squares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2


lower_bound = 10
upper_bound = 20

print(*squares(10, 20))
print()

for squared_number in squares(10, 20):
    print(squared_number, end=" ")
