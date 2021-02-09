T = int(input())
answer = []
for _ in range(T):
    n = int(input())
    dp = [0]*(n+4)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    answer.append(dp[n])
for ans in answer:
    print(ans)