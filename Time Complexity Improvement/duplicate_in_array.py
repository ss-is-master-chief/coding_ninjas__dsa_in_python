def MissingNumber(arr):
    # Please add your code here
    sum = 0
    sum1 = 0
    
    for i in range(n):
        sum = sum + i
        
    for i in range(len(arr)):
        sum1 = sum1 + arr[i]
        
    res = sum - sum1
    return n - 1 - res

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' ')[:n])
ans=MissingNumber(arr)
print(ans)
