n,m = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + arr[i-1][j-1]
print(dp[n][m])
