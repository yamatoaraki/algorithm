buff = [5,2,3,1]

def downheap(buff,x):
    size = len(buff)
    while True:
        children = 2*x+1
        children = int(children)
        if children >= size:
            break
        if children+1 <size:
            if buff[children] > buff[children+1]:
                children = children + 1
        if buff[x] <= buff[children]:
            break
        temp = buff[x]
        buff[x] = buff[children]
        buff[children] = temp
        x = children

for x in range(int(len(buff)/2-1),-1,-1):
    downheap(buff,x)
print(buff)
