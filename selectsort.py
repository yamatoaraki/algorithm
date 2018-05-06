x = [4, 50, 3, 10, 88, 39, 2, 15]

def sSort(a):
    for i in range(len(a)-1):
        mi = a[i:].index(min(a[i:]))
        a[i], a[i+mi] = a[i+mi], a[i]
    print(a)

    return a

sSort(x)
