def get_sum_primes(limit):
    # Create a list of Booleans "True" for every number up to the limit
    primes = [True] * limit
    primes[0] = primes[1] = False # 0 and 1 are not prime
    
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            # If p is prime, mark all its multiples as False
            for i in range(p * p, limit, p):
                primes[i] = False
    
    # Sum all the indices that are still True
    return sum(i for i, is_prime in enumerate (primes) if is_prime)

print(get_sum_primes(10))
