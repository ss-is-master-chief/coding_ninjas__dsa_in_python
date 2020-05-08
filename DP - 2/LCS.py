
def lcsDP(s1, s2, i, j, dp):
#Implement Your Code Here
    if(i==len(s1) or j==len(s2)):
        return 0
    
    if(s1[i]==s2[j]):
        if(dp[i+1][j+1]==-1):
            small_answer = lcsDP(s1, s2, i+1, j+1, dp)
            dp[i+1][j+1] = small_answer
            ans = 1+small_answer
        else:
            ans = 1+dp[i+1][j+1]
    else:
        if(dp[i][j+1]==-1):
            dp[i][j+1] = lcsDP(s1, s2, i, j+1, dp)
            ans1 = dp[i][j+1]
        else:
            ans1 = dp[i][j+1]

        if(dp[i+1][j]==-1):
            dp[i+1][j] = lcsDP(s1, s2, i+1, j, dp)
            ans2 = dp[i+1][j]
        else:
            ans2 = dp[i+1][j]

        ans = max(ans1, ans2)

    return ans
            
        

s1 =input().strip()
s2 =input().strip()
m = len(s1)
n = len(s2)
dp = [[-1 for j in range(n+1)] for i in range(m+1)]
print(lcsDP(s1, s2, 0, 0, dp))