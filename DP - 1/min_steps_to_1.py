import sys
sys.setrecursionlimit(10**6) 

def minStepsTo1DP(n, dp):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if n==1:
        return 0
    
    ans1 = sys.maxsize
    if(n%3==0):
        if(dp[n//3]==-1):
            ans1 = minStepsTo1DP(n//3, dp)
            dp[n//3] = ans1
        else:
            ans1 = dp[n//3]
    
    ans2 = sys.maxsize
    if(n%2==0):
        if(dp[n//2]==-1):
            ans2 = minStepsTo1DP(n//2, dp)
            dp[n//2] = ans2
        else:
            ans2 = dp[n//2]
    
    if(dp[n-1]==-1):
        ans3 = minStepsTo1DP(n-1, dp)
        dp[n-1] = ans3
    else:
        ans3 = dp[n-1]
        
    return 1 + min(ans1, ans2, ans3)
    
# Main
n=int(input())
dp = [-1 for i in range(n+1)]
print(minStepsTo1DP(n, dp))
