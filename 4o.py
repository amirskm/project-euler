def get_largest_palindrome(digits):
    upper_bound = 10**digits - 1
    lower_bound = 10**(digits - 1)
    max_palindrome = 0

    # Start from the largest possible numbers and work down
    for i in range(upper_bound, lower_bound - 1, -1):
        # Optimization: if i * i is smaller than the best palindrome found, 
        # no need to check further for this i
        if i * i <= max_palindrome:
            break
            
        for j in range(i, lower_bound - 1, -1):
            product = i * j
            
            # If product is smaller than what we already found, stop the inner loop
            if product <= max_palindrome:
                break
                
            if is_palindrome(product):
                max_palindrome = product
                
    return max_palindrome

def is_palindrome(val):
    s = str(val)
    return s == s[::-1]

print(get_largest_palindrome(3))
