sum_of_pairs = 0

for y in range(1, 10000):
    pair_sum_1 = 0
    pair_sum_2 = 0
    for x in range(1, y):
        if y % x == 0:
            pair_sum_1 += x

    for b in range(1, pair_sum_1):
        if pair_sum_1 % b == 0:
            pair_sum_2 += b   

    if y == pair_sum_2 and pair_sum_2 != pair_sum_1:
        sum_of_pairs += pair_sum_1 + pair_sum_2
        print('pair_sum_1', pair_sum_1)
        print('pair_sum_2', pair_sum_2)
        print('sum', sum_of_pairs)