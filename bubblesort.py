x = [4,50,3,10,88,39,15,2]
for y in range(len(x)):
    for i in range(1,len(x)):
        j = len(x)-i
        a = x[j]
        b = x[j-1]
        if a < b:
            x[j-1]=a
            x[j]=b
print(x)
