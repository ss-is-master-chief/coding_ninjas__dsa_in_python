import heapq
def checkMaxHeap(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    heap = lst.copy()
    heapq._heapify_max(heap)
    if(heap==lst):
        return True
    return False

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
