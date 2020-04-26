import sys
sys.setrecursionlimit(10**6) 

def minSquares(n):
    #Implement Your Code Here
    if(n==0):
        return 0
    ans = sys.maxsize
    for i in range(1, int(n**0.5) + 1):
        checkValue = n-i**2
        if(dp[checkValue]==-1):
            smallValue = minSquares(checkValue)
            dp[checkValue] = smallValue
            curr_ans = 1+smallValue
        else:
            curr_ans = 1+dp[checkValue]
        ans = min(ans, curr_ans)
    return ans

    
n = int(input())
dp = [-1 for i in range(n+1)]
ans = minSquares(n)
print(ans)


