x = [4,50,3,10,88,39,2,15]

for i in range(1,len(x)):
    #j = i
    while (i > 0) and (x[i-1] > x[i]) :
        tmp = x[i-1]
        x[i-1] = x[i]
        x[i] = tmp
        i -= 1
    print (x)

print ("-"*30)
print (x)
