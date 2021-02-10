import math
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
dp = [[0]*n for i in range(n)]
for j in range(1,n):
    for i in range(j-1,-1,-1):
        if j-i == 1:
            dp[i][j] = matrix[i][0] * matrix[i][1] * matrix[j][1]
            continue
        small = math.inf
        for k in range(j-i):
            small = min(small, dp[i][i+k] + dp[i+k+1][j] + matrix[i][0]*matrix[i+k][1]*matrix[j][1])
        dp[i][j] = small
print(dp[0][n-1])