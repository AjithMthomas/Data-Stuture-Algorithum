# __name__ is  special variable in python which is used to find find the current project file 
# if we want to find the execution started file we can use print(__name__) current executing file will be __main__
# and the others will be results their file name it self

pi =3.14

def Value_of_Pi():
    return pi

def Perimeter(r):
    return 2*pi*r


if __name__ == '__main__':
    print('this is from circle')



