## Read input as specified in the question.
## Print output as specified in the question.
def recursiveMultiply(a, b):
    if(a==0 or b==0):
        return 0
    if(b==1):
        return a
    return a + recursiveMultiply(a, b-1) 

a = int(input())
b = int(input())

rmult = recursiveMultiply(a, b)
print(rmult)