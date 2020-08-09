#######################################
#alg1
#######################################
def ALG1(A,n,i):
    InsertionSort(A,n,i)
    print(A[i])
    
def InsertionSort(A,n,i):
    for j in range(1, len(A)): #from the second postition in the array to the the length of the array
        key = A[j]
        #insert A[j] into the sorted sequence A[1...j-1]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key 

#######################################
#alg2
#######################################        
def ALG2(A,n,i):
    HeapSort(A)
    print(A[i])

def HeapSort(A):
    AheapSize=0
    n = AheapSize = len(A) #heapSize?
    BuildMaxHeap(A) #need to make this 
    for i in range(n-1, 1, -1): #start,stop,step
        A[i], A[0] = A[0], A[i] #swap
        AheapSize = AheapSize - 1
        MaxHeapify(A,1) #need to make

def BuildMaxHeap(A):
    AheapSize=0
    n = AheapSize = len(A)
    for i in range(int(n/2), 1):
        MaxHeapify(A,i)

def MaxHeapify(A,i):
    AheapSize=0
    n = AheapSize
    l = 2*i+1 #Left(i)
    r = 2*i+2 #Right(i)
    if l<=n and A[l]>A[i]:
        larget = l
    else:
        largest = i
    if r<=n and A[r]>A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i] #exchange A[i] with A[largest]
        MaxHeapify(A, largest)

# #driver code to test out ALG2()
# A = [10, 20, 9, 15, 3000]
# HeapSort(A)
# n = len(A)
# print('sorted HeapSort() array is:')
# for i in range(n):
#     print ('%d' %A[i])

#######################################
#alg3
#######################################
#import random

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

# #driver code
# A = [10, 20, 9, 15, 3000]
# n = len(A)
# i=0
# ALG3(A,n,i)


#######################################
#main
#######################################

import random
from timeit import default_timer as timer

def main():
    A = [[],[],[],[],[]]
    
    #And then use two for loops to add random values to A.
    # The syntax would look something like:
    for index in range(0,5):
        for j in range(0,20):
            someRandomValue = random.randint(0, 20000, 1000) # 1 ## needs to be 32767
            A[index].append(someRandomValue) # 2 

    #measurements for alg1
    for n in range(10, n<=20, n+100):
        floor = 2*n / 3
        i = floor
        for j in range(1, int(n>=j), j+1): #4
            B[1,n] = A[j,n-1]
            t1 = timer()
            ALG1(A,n,i) #ALG1(B,n,i) # 3 
            t2 = timer()
            tALG1[j,n] = t2 - t1  #RT for ALG1(), insertionsort

    #measurement alg2
    for n in range(10, n<=20, n+100):
        floor = 2*n / 3
        i = floor
        for j in range(1, int(n>=j), j+1): #4
            B[1,n] = A[j,n-1]
            t3 = timer()
            ALG2(A,n,i)  
            t4 = timer()
            tALG2[j,n] = t3 - t4  

    #measurement alg3
    for n in range(10, n<=20, n+100):
        floor = 2*n / 3
        i = floor
        for j in range(1, int(n>=j), j+1): #4
            B[1,n] = A[j,n-1]
            t5 = timer()
            ALG3(A,n,i)  
            t6 = timer()
            tALG3[j,n] = t5 - t6
            
    #compute average
    #tAvgALG1[n] = ((tALG1[1,n] + tALG1[2,n] + ... + tALG1[m,n]) / (m))  

 




if __name__ == "__main__":
    main()