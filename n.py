def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0
print(is_power_of_2(4))