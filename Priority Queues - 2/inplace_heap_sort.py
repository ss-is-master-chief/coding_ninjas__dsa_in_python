## Read input as specified in the question.
## Print output as specified in the question.

def percolateDown(values, i, n):
    parentIndex = i
    leftChildIndex = 2*parentIndex+1
    rightChildIndex = 2*parentIndex+2
    
    while leftChildIndex < n:
        minIndex = parentIndex
        
        if(values[minIndex]> values[leftChildIndex]):
            minIndex = leftChildIndex
        
        if(rightChildIndex<n and values[minIndex]>values[rightChildIndex]):
            minIndex = rightChildIndex
            
        if(minIndex==parentIndex):
            return
        
        values[minIndex], values[parentIndex] = values[parentIndex], values[minIndex]
        parentIndex = minIndex
        
        leftChildIndex = 2*parentIndex+1
        rightChildIndex = 2*parentIndex+2
    
    return

def heapSort(values, n):
    
    n = len(values)
    # Building the heap
    for i in range(n//2, -1, -1):
        percolateDown(values, i, n)
        
    # Sorting the heap
    for i in range(n-1, 0, -1):
        values[0], values[i] = values[i], values[0]
        percolateDown(values, 0, i)
    
    return
    

n = int(input())
values = [int(x) for x in input().rstrip().split(' ')]
heapSort(values, n)
for i in values:
    print(i, end=" ")