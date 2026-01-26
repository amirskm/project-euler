def get_square_digit(n):

    square_sum = 0

    for i in range(0, len(str(n))):
        square_sum += int(str(n)[i])**2

    if square_sum == 1 or square_sum == 89:
        return square_sum
    else:
        return get_square_digit(square_sum)

def get_count_below_limit(limit, destination):
    count = 0
    for j in range(1, limit + 1):
        if get_square_digit(j) == destination:
            count += 1
    return count

print(get_count_below_limit(9999999, 89))