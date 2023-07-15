def Right_Triangle(s1,s2,s3):
    list1=[s1,s2,s3]
    list1.sort(reverse=True)
    sumOfSqareOfSmallSides = (list1[1]**2)+(list1[2]**2)
    if sumOfSqareOfSmallSides == list1[0]**2:
        print('right angle triangle')
    else:
        print('not right angled triangle')


Right_Triangle(3,4,5)
