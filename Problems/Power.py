def power_mod(x, y, n):
    y %= n 
    return(x**y) % n

print(power_mod(2, 3, 5))
print(power_mod(4, 12, 3))
print(power_mod(11, 10, 300))
print(power_mod(11, 10000000, 49))
print(power_mod(5, 10000000000, 19))

