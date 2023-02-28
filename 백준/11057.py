n = int(input())
dp = [[0]*10 for i in range(1001)]
for i in range(10):
    dp[1][i] = 1
for i in range(2,1001):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
            continue
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])

print(sum(dp[n]) % 10007)