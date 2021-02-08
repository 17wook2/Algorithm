n = int(input())
# 현재 상태에서 3가지
dp = [0] * (n+3)
dp[2] = 1
dp[3] = 1
for i in range(4,n+1):
    dp[i] = 1 + dp[i-1]
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
# print(dp)
print(dp[n])