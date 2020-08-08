def ALG1(A,n,i):
    InsertionSort(A,n,i)

def InsertionSort(A,n,i):
    for j in range(1, len(A)): #from the second postition in the array to the the length of the array
        key = A[j]
        insert A[j] into the sorted sequence A[1...j-1]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key 
    
        
def ALG2(A,n,i):
    HeapSort(A,n,i)

def HeapSort(A,n,i):
    n = AheapSize = len(A) #heapSize?
    BuildMaxHeap(A,n,i) #need to make this 
    for i in range(n-1, 1, -1): #start,stop,step
        A[i], A[0] = A[0], A[i] #swap
        AheapSize = AheapSize - 1
        MaxHeapify(A,n,1) #need to make

    #driver code to test out ALG2()
    A = [10, 20, 9, 15, 3000]
    HeapSort(A,n,i)
    n = len(A)
    print('sorted HeapSort() array is:')
    for i in range(n):
        print ('%d' %A[i])

def BuildMaxHeap(A,n,i):
    n = AheapSize = len(A)
    for i in range(n/2, 1):
        MaxHeapify(A,n,i)

def MaxHeapify(A,n,i):
    n = AheapSize
    l = Left[i]
    r = Right[i]
    if l<=n and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r<=n and A[r]>A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i] #exchange A[i] with A[largest]
        MaxHeapify(A, largest)


import random
from timeit import default_timer as timer

def main():
    A = [[],[],[],[],[]]
    
    #And then use two for loops to add random values to A.
    # The syntax would look something like:
    for index in range(0,5):
        for j in range(0,20):
            someRandomValue = random.randint(0, 100) # 1 ## needs to be 32767
            A[index].append(someRandomValue) # 2 

    #measurements for alg1
    #n = 10
    for n in range(10, n<=20, n+100):
        floor = 2*n / 3
        i = floor
        for j in range(1, int(m>=j), j+1): #4
            B[1,n] = A[j,n-1]
            t1 = timer()
            ALG1(A,n,i) #ALG1(B,n,i) # 3 
            t2 = timer()
            tALG1[j,n] = t2 - t1  #RT for ALG1(), insertionsort

    #measurement alg2

    #measurement alg3

    #compute average
    #tAvgALG1[n] = ((tALG1[1,n] + tALG1[2,n] + ... + tALG1[m,n]) / (m))  

 




# if __name__ == "__main__":
#     main()