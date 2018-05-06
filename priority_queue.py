class PQueue:
    def __init__(self, buff = []):
        self.buff = buff[:]
        for n in range(int(len(self.buff) / 2) - 1, -1, -1):
            downheap(self.buff, n)
        print(self.buff)

    # データの追加
    def push(self, data):
        self.buff.append(data)
        upheap(self.buff, len(self.buff) - 1)

    # 最小値を取り出す
    def pop_original(self):
        if len(self.buff) == 0: raise IndexError
        value = self.buff[0]
        last = self.buff.pop()
        if len(self.buff) > 0:
            # ヒープの再構築
            self.buff[0] = last
            downheap(self.buff, 0)
        return value



    def peek(self):
        if len(self.buff) == 0: raise IndexError
        return self.buff[0]

    def isEmpty(self):
        return len(self.buff) == 0

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

if __name__ == '__main__':
    import random
    #a = PQueue()
    #for x in range(10):
        #n = random.randint(0, 100)
        #a.push(n)
        #print (n, 'min data = ', a.peek())
    #while not a.isEmpty():
        #print (a.pop())
    data = [42,94,81,43,56,65]
    print (data)
    a = PQueue(data)
    while not a.isEmpty():
        print (a.pop_original())
