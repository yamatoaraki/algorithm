buff = [2,5,1,5,4,9,12,7,8]

def upheap(buff,x):
    while True:
        parent = (x-1)/2
        parent = int(parent)
        if parent < 0 or buff[parent] <= buff[x]:
            break
        temp = buff[parent]
        buff[parent] = buff[x]
        buff[x] = temp
        x = parent

for x in range(1,len(buff)):
    upheap(buff,x)
print(buff)
