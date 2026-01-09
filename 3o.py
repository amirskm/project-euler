def sum_squared_natural_numbers(count):
    n = 0
    sum_squared_total = 0
    while n <= count:
        sum_squared_total += n ** 2
        n += 1
    return sum_squared_totalgit

def square_sum_natural_numbers(count):
    n = 0
    square_sum_total = 0
    while n <= count:
        square_sum_total += n
        n += 1
    return square_sum_total**2
# def get_sum_and_square_difference(count)

print(square_sum_natural_numbers(100) - sum_squared_natural_numbers(100))