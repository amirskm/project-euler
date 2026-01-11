def sum_squared_natural_numbers(count):
    return sum(n**2 for n in range(1, count + 1))

def square_sum_natural_numbers(count):
    return (sum(range(count + 1)))**2

print(square_sum_natural_numbers(100) - sum_squared_natural_numbers(100))