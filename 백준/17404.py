import math
n = int(input())
colors = []
dp = [[math.inf]*3 for i in range(n)]
for i in range(n):
    colors.append(list(map(int,input().split())))
ans = math.inf
for k in range(3): # 처음 고르는 색
    for i in range(3):
        if i == k:
            dp[0][i] = colors[0][i]
        else:
            dp[0][i] = math.inf
    for i in range(1,n):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + colors[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + colors[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + colors[i][2]
    for i in range(3):
        if i == k:
            continue
        ans = min(ans,dp[n-1][i])
print(ans)