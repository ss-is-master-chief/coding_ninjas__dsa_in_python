def equilibriumIndex(arr):
    # Please add your code here
    num = len(arr)
    total = 0
    sum_left = 0
    for i in range(0, num):
        total = total + arr[i]
    for i in range(0, num):
        total = total - arr[i]
        if (sum_left == total):
            return i
        sum_left = sum_left + arr[i]
    return -1

# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))
