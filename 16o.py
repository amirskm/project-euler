def get_power_digit_sum(base, power): 
    power_digit = base ** power
    power_digit_sum = 0
    for i in range(0, len(str(power_digit))):
        power_digit_sum += int(str(power_digit)[i])
    return power_digit_sum

print(get_power_digit_sum(2, 1000))