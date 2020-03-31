def arrayIntersection(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i,j = 0,0
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] < arr2[j]: 
            i += 1
        elif arr2[j] < arr1[i]: 
            j+= 1
        else: 
            print(arr2[j]) 
            j += 1
            i += 1


m = int(input())
arr1 = [int(x) for x in input().split(' ')[:m]]

n = int(input())
arr2 = [int(x) for x in input().split(' ')[:n]]


arrayIntersection(arr1, arr2)


