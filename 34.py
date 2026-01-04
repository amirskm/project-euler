import math 

digit = 0
factorial_sum = 0
curious_number_sum = 0 

# print(int(str(n)[2]))

for potential_curious_number in range(0, 10000000):
    factorial_sum = 0
    for digit in range(0, len(str(potential_curious_number))):
        factorial_sum += math.factorial(int(str(potential_curious_number)[digit]))
        if potential_curious_number == factorial_sum:
            print('potential_curious_number', potential_curious_number)
            curious_number_sum += potential_curious_number
print('curious_number_sum', curious_number_sum - 3)