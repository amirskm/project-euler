from math import factorial

def get_factorial_digit_sum(limit):
    factorial_calc = factorial(limit)
    s = 0
    for n in range(0, len(str(factorial_calc))):
        s += int(str(factorial_calc)[n])
    return s


    
print(get_factorial_digit_sum(100))