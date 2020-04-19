import heapq
def kLargest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    heap = lst[:k]
    heapq.heapify(heap)
    for i in range(k, len(lst)):
        if(heap[0]<lst[i]):
            heapq.heapreplace(heap, lst[i])
    return heap

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
