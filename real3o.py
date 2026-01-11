def get_largest_prime_factor(n):
    factor = 
    while factor < n ** .5 + 1:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

print(get_largest_prime_factor(600851475143))