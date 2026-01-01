x = 1
y = 1

while x < 20:
    if y % x == 0:
        x = x + 1 
    else:
        y = y + 1
        x = 1
print(y)