# *a represents the arbitory positional argument
# a will be a tuple 
def AddNumbers(*a):
    sum = 0
    for i in  a:
        sum += i
    print(sum)

AddNumbers(1,2,4,54,4)

    