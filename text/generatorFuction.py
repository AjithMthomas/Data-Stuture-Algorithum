def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Using the generator function to print numbers up to 5
generator = count_up_to(5)
for num in generator:
    print(num)
