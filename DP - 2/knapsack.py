
def knapsackBF(weights, values, maxWeight, n, i):
    #Implement Your Code Here
    if(i==n):
        return 0
    if(weights[i]>maxWeight):
        ans = knapsackBF(weights, values, maxWeight, n, i+1)
    else:
        ans1 = values[i] + knapsackBF(weights, values, maxWeight-weights[i], n, i+1)
        ans2 = knapsackBF(weights, values, maxWeight, n, i+1)
        ans = max(ans1, ans2)
    return ans

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
weights=list(int(i) for i in input().strip().split(' '))
values=list(int(i) for i in input().strip().split(' '))
maxWeight=int(input())
n = len(values)
print(knapsackBF(weights, values, maxWeight, n, 0))