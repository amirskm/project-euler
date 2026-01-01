for a in range(1, 1000):
    b = (1000 * (500 - a)) / (1000 - a)
    if a < b and (1000 * (500 - a)) % (1000 - a) == 0:
        c = (b**2 + a**2)**.5
        if c + b + a == 1000:
            print('a', a)
            print('b', b)
            print('c', c)
            print('prod', c*b*a)
            print('---')