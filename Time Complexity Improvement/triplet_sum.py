def findTriplet(arr, sumVal):
    for i in range(0, len(arr)-2): 
        for j in range(i + 1, len(arr)-1):  
            for k in range(j + 1, len(arr)): 
                if arr[i] + arr[j] + arr[k] == sumVal: 
                    print(arr[i], arr[j], arr[k]) 
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sumVal = int(input())
findTriplet(arr, sumVal)
