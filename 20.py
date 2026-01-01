n = 100
y = 1
a = 0

for x in range(1, n + 1):
    y = x * y
print(y)

for z in range(0, len(str(y))):
    a = int(str(y)[z]) + a
print(a)