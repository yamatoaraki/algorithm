def parent(i):
    return i/2

def left(i):
    return 2*i

def right(i):
    return 2*i+1

def maxHeapify(A,i):
    l = left(i)
    r = right(i)
    if l <= H and A[l] > A[i]:
        largest =  l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r

    if largest != i:
        maxHeapify(A,largest)

def buildMaxHeap(A):
    for i in reversed(range(1,10)):
        maxHeapify(A,i)

A = [4,1,3,2,16,9,10,14,8,7]
H =10
buildMaxHeap(A)
