import sys
import math
input = sys.stdin.readline
n = int(input())
m = int(input())
dp = [[math.inf]*n for i in range(n)]
for i in range(m):
    a,b,c = list(map(int,input().split()))
    if dp[a-1][b-1] != math.inf:
        dp[a-1][b-1] = min(dp[a-1][b-1], c)
    else:
        dp[a-1][b-1] = c
for i in range(n):
    dp[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
for i in range(n):
    for j in range(n):
        if dp[i][j] == math.inf:
            dp[i][j] = 0

for row in dp:
    print(*row)