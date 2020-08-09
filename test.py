import random

def ALG3(A,n,i):
 x = RandomSelect(A,1,n,i)
 print(x)

def RandomSelect(A,p,r,i):
    if p==r:
        return A[p]
    q=RandomizedPartition(A,p,r)
    k= q-p+1
    if i==k:
        return A[q]
    elif i<k:
        return RandomSelect(A,p,q-1,i)
    else: #i>k
        return RandomSelect(A,q+1,r,i-k)

def RandomizedPartition(A,p,r):
    i = Random(p,r)
    A[r], A[i] = A[i], A[r]
    return Partition(A,p,r)

def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(j=p, r=r-1):
        if A[j]<=x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def Random(p,r):
    someRandomValue = random.randint(0, 100)
    return someRandomValue

#driver code
A = [10, 20, 9, 15, 3000]
n = len(A)
i=0
ALG3(A,n,i)
