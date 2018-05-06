def upheap(buff, n):
    while True:
        p = (n - 1) / 2
        p = int(p)
        if p < 0 or buff[p] <= buff[n]:
            break
        temp = buff[n]
        buff[n] = buff[p]
        buff[p] = temp
        n = p
buff = [2,5,1,5,4,9,12,7,8]
for x in range(1, len(buff)):
    upheap(buff, x)
print(buff)

def recreateheap(buff, n):
    size = len(buff)
    while True:
        c = 2 * n + 1
        c = int(c)
        if c >= size:
            break
        if c + 1 < size:
            if buff[c] > buff[c + 1]:
                c += 1
        if buff[n] <= buff[c]:
            break
        temp = buff[n]
        buff[n] = buff[c]
        buff[c] = temp
        n = c
buff.append(1)
for x in range(int(len(buff) / 2 - 1), -1, -1):
    recreateheap(buff, x)

print(buff)
