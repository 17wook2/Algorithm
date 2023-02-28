n = int(input())
arr = list(map(int,input().split()))
dp = [1001]*(n+101)
dp[0] = 0
for i in range(n):
    k = arr[i]
    for j in range(1,k+1):
        dp[i+j] = min(dp[i+j],dp[i] + 1)
if dp[n-1] == 1001:
    print(-1)
else:
    print(dp[n-1])