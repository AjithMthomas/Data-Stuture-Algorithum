a=[9,8,6,78,93]
pivot=a[-1]
b=[]
c=[]
for i in a:
    if i<pivot:
        b.append(i)
    elif i>pivot:
        c.append(i)
