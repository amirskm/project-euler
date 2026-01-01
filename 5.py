n = 101
j = 0
y = 0
for i in range(1, n):
    j = i**2 + j
print(j)

for x in range(1, n):
    y += x
print(y**2)

z = y**2 - j
print(z)