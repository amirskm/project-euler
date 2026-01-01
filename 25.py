x = 1
y = 1
i = 0

while len(str(x)) < 1000:
    x = x + y
    y = x - y
    i += 1
print(i + 2)
# print(x)