def sumArray(arr, n):
    # Please add your code here
    if(n==1):
        return arr[0]
    return arr[n-1]+sumArray(arr, n-1)
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr, n))
