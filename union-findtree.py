import random
import time
class UnionFind1:
    def __init__(self, size):

        self.table = [-1 for _ in range(size)]


    def find(self, x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x


    def union(self, x, y):
        s1 = self.find(x)
        print(self.table[s1])
        s2 = self.find(y)
        print(self.table[s2])
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            print(self.table)
            return True
        return False
def test_union(func, data,size):
    a = time.clock()
    for x, y in data:
        func(x, y)
    print(A.table)
    print (time.clock() - a)
A = UnionFind1(6)
data = [(random.randint(0, 6 - 1), random.randint(0, 6 - 1)) for _ in range(6)]
print(A.table)
print(data)
test_union(A.union, data,6)
