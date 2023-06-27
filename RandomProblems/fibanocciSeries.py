def is_perfect_square(n):
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

def is_fibonacci_number(x):
    if x == 0 or x == 1:
        return True
    
    check1 = 5 * x * x + 4
    check2 = 5 * x * x - 4
    
    return is_perfect_square(check1) or is_perfect_square(check2)


number = int(input("Enter a number: "))
if is_fibonacci_number(number):
    print(number, "is a Fibonacci number.")
else:
    print(number, "is not a Fibonacci number.")
