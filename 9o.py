def product_of_triplet(triplet_sum):
    a = 3
    b = 4
    c = (b**2 + a**2)**.5
    
    for a in range(triplet_sum//3, 1, -1):
        for b in range(triplet_sum//2, a + 1, -1):
            c = (b**2 + a**2)**.5
            if a < b < c and a + b + c == triplet_sum:
                return(f"a is {a}, b is {b}, c is {c}, and product is {a * b * c}")
 
print(product_of_triplet(1000))