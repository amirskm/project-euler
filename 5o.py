def get_smallest_multiple(largest_factor):
    # Start at the largest factor, and jump by that factor every time
    n = largest_factor
    while True:
        # Check factors in reverse (20, 19, 18...) because 
        # large numbers are more likely to fail the check sooner
        if all(n % m == 0 for m in range(largest_factor, 1, -1)):
            return n
        n += largest_factor

print(get_smallest_multiple(20))how