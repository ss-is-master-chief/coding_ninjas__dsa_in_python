def FindUnique(arr):
    # Please add your code here
    res = arr[0]
    for i in range(1, len(arr)):
        res = res ^ arr[i]
    return res

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr)
print(unique)
