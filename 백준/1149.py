N = int(input())
dp = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,N):
    for j in range(3):
        if j == 0:
            dp[i][j] += min(dp[i-1][j+1], dp[i-1][j+2])
        elif j == 1:
            dp[i][j] += min(dp[i-1][j-1],dp[i-1][j+1])
        elif j == 2:
            dp[i][j] += min(dp[i-1][j-2], dp[i-1][j-1])
print(min(dp[N-1]))