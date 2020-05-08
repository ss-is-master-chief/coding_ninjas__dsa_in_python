## Read input as specified in the question.
## Print output as specified in the question.

import sys

def min_cost(cost, n, m):
    dp_matrix = [[sys.maxsize for ni in range(n+1)] for mi in range(m+1)]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if(i==m-1 and j==n-1):
                dp_matrix[i][j] = cost[i][j]
            else:
                ans1 = dp_matrix[i+1][j+1]
                ans2 = dp_matrix[i][j+1]
                ans3 = dp_matrix[i+1][j]
                dp_matrix[i][j] = min(ans1, ans2, ans3) + cost[i][j]
    return dp_matrix[0][0]
                

m, n = [int(x) for x in input().rstrip().split(' ')]
cost = [[int(x) for x in input().rstrip().split(' ')] for mi in range(m)]

print(min_cost(cost, n, m))