from math import isqrt

triangle_num = 0
#n = 20000
n = 0
factor_count = 0 
# for natural_num in range(0, n + 1):
#     triangle_num += natural_num

while factor_count < 500:
    n += 1
    factor_count = 0
    triangle_num = n * (n + 1) // 2 
    # print('triangle_num', triangle_num)

    for factor in range(1, isqrt(triangle_num) + 12):
        if triangle_num % factor == 0:
        #  print('factor', factor)
            factor_count += 2
print('triangle_num', triangle_num)
print('factor_count', factor_count)
print('n', n)



# n = 0 
# factor_count = 6
# triangle_num = 0
# y = 0 

# for x in range(0, 10):
#     y += x
# print(y)