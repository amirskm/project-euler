def get_sum_primes(limit):
    limit_sum = 2
    for n in range(3, limit, 2):
        if all(n % d != 0 for d in range(3, int(n**.5 + 1), 2)):
            print(n)
            limit_sum += n
    return limit_sum 

print(get_sum_primes(2000000))