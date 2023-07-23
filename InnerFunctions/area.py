# we want to find the area of a circle and a rectangle using inner function
def area(r,l,b):
    def area_of_rectangle(l,b):
        return l*b
    def area_of_circle(r):
        pi = 3.14 
        return pi*r*r
    return area_of_rectangle(l,b) + area_of_circle(r)

area = area(10,10,10)
print(area)