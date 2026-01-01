x = 2
y = 2

count = 1 
while count < 10002:
    if any((x % y == 0) for y in range(2, x)):
        x += 1
    else:
        print(count)
        count += 1 
        print('prime x', x)
        x += 1