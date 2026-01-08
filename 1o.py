def get_sum_of_multiples(limit, *divisors):
    total = 0
    for nautral_numbers in range(1, limit):
        if any((nautral_numbers % multiples == 0) for multiples in divisors):
                total += nautral_numbers
                print(nautral_numbers)
    return total

print(get_sum_of_multiples(1000, 3, 5))