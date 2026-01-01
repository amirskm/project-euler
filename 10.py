s = 0
for t in range(3, 10, 2):
    for y in range(3, int(t**.5) + 1, 2):
        if t % y == 0:
            break
    else:
        print(t)
        s += t
print(s + 2)
