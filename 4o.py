def get_largest_palindrom(digits):
    n = 1
    p = get_largest_potential_palindrom(digits)
    while n < p:
        if is_palindrome(p) and is_factors_length(digits, p):
            return p
            break
        else:
            p += -1

def is_factors_length(length, palindrom):
    for n in range(10**(length - 1), 10**length):
        if palindrom % n == 0 and len(str(palindrom // n)) == length:
            return True
            break
    return False

def is_palindrome(val):
    s = str(val)
    return s == s[::-1]

def get_largest_potential_palindrom(length):
    return int((9 * (10 ** length - 1) / (10 - 1))**2)

print(get_largest_palindrom(3))