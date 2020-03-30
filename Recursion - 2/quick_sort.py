def partition(arr, si, ei):
    pivot = arr[si]
    c = 0
    for i in range(si, ei+1):
        if(arr[i]<pivot):
            c += 1

    arr[si+c], arr[si] = arr[si], arr[si+c]
    pivot_index = si + c
    i = si
    j = ei
    
    while(i<j):
        if(arr[i]<pivot):
            i += 1
        elif arr[j]>=pivot:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return pivot_index  

def quickSort(arr, si, ei):
    if(si>=ei):
        return
  
    pivot_index = partition(arr, si, ei)
    quickSort(arr, si, pivot_index-1)
    quickSort(arr, pivot_index+1, ei)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
