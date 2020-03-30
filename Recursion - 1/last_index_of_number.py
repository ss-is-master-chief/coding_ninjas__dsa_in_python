## Read input as specified in the question.
## Print output as specified in the question.

def lastIndex(arr, x):
    if(len(arr)==0):
        return -1
    if(arr[len(arr)-1]==x):
        return len(arr)-1
    return lastIndex(arr[:len(arr)-1], x)

import sys
sys.setrecursionlimit(11000)

n = int(input())
arr = [int(ele) for ele in input().strip().split(" ")]
x = int(input())

print(lastIndex(arr, x))