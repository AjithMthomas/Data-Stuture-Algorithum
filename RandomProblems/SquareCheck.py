def array(array1,array2):
    for i in array1:
        for j in array2:
            if i*i in array2:
                return(True)
            return(False)
array1=[1,2,4]
array2=[1,4,15]
print(array(array1,array2))