def get_square_digit(n):
    # Convert to string to access individual digits
    first = int(str(n)[0])
    second = int(str(n)[1])

    # Calculate the product (or square logic) and return it
    result = first * second
    return result

print(get_square_digit(14))
