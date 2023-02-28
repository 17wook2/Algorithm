t = int(input())
dp = [0]*10001
dp[0] = 1
for i in range(1,4):
    for j in range(1,10001):
        if j >= i:
            dp[j] += dp[j-i]

for _ in range(t):
    n = int(input())
    print(dp[n])