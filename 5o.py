import math 

def get_smallest_multiple(largest_factor):
    for n in range(1, math.factorial(largest_factor)):
        if all(n % m == 0 for m in range(1, largest_factor)):
            return n

print(get_smallest_multiple(20))