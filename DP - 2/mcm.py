import sys

def mcm(ele, i, j, dp):
    if(i==j):
        return 0

    min_value = sys.maxsize
    for k in range(i, j):
        if(dp[i][k]==-1):
            ans1 = mcm(ele, i, k, dp)
            dp[i][k] = ans1
        else:
            ans1 = dp[i][k]
        
        if(dp[k+1][j]==-1):
            ans2 = mcm(ele, k+1, j, dp)
            dp[k+1][j] = ans2
        else:
            ans2 = dp[k+1][j]
        
        mCost = ele[i-1]*ele[k]*ele[j]
        curr_value = ans1 + ans2 + mCost
        min_value = min(min_value, curr_value)
        
    return min_value

n = int(input())
ele = [int(x) for x in input().strip().split(' ')]
n = len(ele)-1
dp = [[-1 for j in range(n+1)] for i in range(n+1)]
ans = mcm(ele, 1, n, dp)
print(ans)