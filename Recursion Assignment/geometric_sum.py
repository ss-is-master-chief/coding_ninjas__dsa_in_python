## Read input as specified in the question.
## Print output as specified in the question.

def geometricSum(n):
    if(n==0):
        return 1
    val = 1/(2**n)
    return val+geometricSum(n-1)


n = int(input())
print("{:.5f}".format(geometricSum(n)))
