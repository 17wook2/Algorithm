n,m = map(int,input().split())
memory = list(map(int,input().split()))
costs = list(map(int,input().split()))
max_cost = sum(costs)
dp = [[0]*10100 for i in range(101)]
ans = sum(costs)
for i in range(n):
    for j in range(max_cost+1):
        if costs[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i-1]] + memory[i-1])
        if dp[i][j] >= m:
            ans = min(ans,j)
print(ans)