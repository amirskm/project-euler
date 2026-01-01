t = 0

while True:
    y = 0
    factors = 0 
    t += 1

    for n in range(1, t):
        y += n
    
    for z in range(1, y + 1):
        if y % z == 0:
            factors += 1
                
    if factors > 501:
        print(y)
        break