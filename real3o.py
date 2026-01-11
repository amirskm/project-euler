def get_largest_prime_factor(n):
    largest_factor = 0
    for factor in range(2, int(n**.5 + 1)):
        if (n % factor == 0) and all(factor % i != 0 for i in range(2, int(factor**.5 + 1))):
            largest_factor = factor
    return largest_factor

print(get_largest_prime_factor(600851475143))