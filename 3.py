for x in range(100000, 999*999):
    if (str(x)[0] == str(x)[5]) and (str(x)[1] == str(x)[4]) and (str(x)[2] == str(x)[3]): 
        #print(x)
        for y in range(100, 999):
            if x % y == 0 and len(str(int(x / y))) == 3:
                print(len(str(int(x / y))))
                print(x/y)
                print(y) 
                print(x)
