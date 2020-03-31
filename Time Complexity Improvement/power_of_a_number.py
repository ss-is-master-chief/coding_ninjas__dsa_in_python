def power(x, n):
    # Please add your code here
    if(n==0):
        return 1
    if(n%2==0):
        small_output = power(x, n/2)
        return small_output**2
    else:
        small_output = power(x, n//2)
        return small_output**2 * x

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
