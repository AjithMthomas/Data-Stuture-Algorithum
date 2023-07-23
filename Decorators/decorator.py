# decorator is used to give a additional fuctionality to a existing function 
# without changing it , think that programmers are working in different modules and we want to add
# a additonal fuctionality to a fuction which is created by anther programmer, we cannot change the fuction ceacted by the programmer
# in this case we can use decorators

from area import area

def decorator(function):
    def inner(r):
        if r>100:
            r=100
        return function(r)
    return inner

area =decorator(area)
print(area(102))