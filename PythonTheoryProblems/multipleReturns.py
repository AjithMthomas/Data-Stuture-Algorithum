def values(a:list):
    f = lambda a:a*a
    new= [f(i) for i in a]
    sum = 0
    for i in new:
        sum+=i
    return new,sum

new,sum =values([1,2,3,4,5])
print(f"sum is {sum}, new list is {new}")
    