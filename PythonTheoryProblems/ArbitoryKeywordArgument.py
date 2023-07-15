# **a represents the arbitory keyword argument
# a will be dictionary
def person (**a):
    for key, value in a.items():
        print(key,":",value)


person(name='aji',age=13,salary=100000)