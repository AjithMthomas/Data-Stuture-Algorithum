a=[1,2,3,4]
largest=0
for i in a:
    if i> largest:
        largest = i
        
for i in a:
    if largest < i *2:
        print("True")
    else:
       print ("False")