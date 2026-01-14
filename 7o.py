def get_prime(nth_prime):
    potential_prime = 2
    prime_count = 0
    while prime_count < nth_prime:
        # Check if potential_prime is prime
        if all(potential_prime % factor != 0 for factor in range(2, potential_prime)):
            prime_count += 1
        
        # Move this OUTSIDE the if-statement so we always move to the next number
        potential_prime += 1
        
    # Subtract 1 because the loop adds 1 even after finding the target prime
    return potential_prime - 1

print(get_prime(10001)) # Output: 5
