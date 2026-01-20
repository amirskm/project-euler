def get_fibonacci_number(digits):
    f_one = 1
    f_two = 1
    index = 1
    while len(str(f_one)) < digits:
        f_two = f_one + f_two 
        f_one = f_two - f_one
        index += 1
    return index

print(get_fibonacci_number(1000))