num = 2**1000
y = 0

for x in range(0, len(str(num))):
    y += int(str(num)[x])
    print(str(num)[x])

print(y)