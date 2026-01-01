x = 600851475143
i = 1
j = 1

while i < x:
    i = i + 1
    if all(i % j != 0 for j in range(2, i)) and (x % i == 0):
        print(i)    