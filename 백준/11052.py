n = int(input())
cost = list(map(int,input().split()))
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i] = cost[i-1]
for i in range(2,n+1):
    for j in range(1,i):
        dp[i] = max(dp[i], dp[i-j] + dp[j])
print(dp[n])
