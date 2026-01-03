for x in range(1, 1000000):
    sum_of_fourth_powers = 0
    for y in range(0, len(str(x))):
        sum_of_fourth_powers += int(str(x)[y])**5
    if x == sum_of_fourth_powers:
        print(x)