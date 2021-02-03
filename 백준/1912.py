N = int(input())
lst = list(map(int,input().split()))
dp = [0] * N
dp[0] = lst[0]
for i in range(1,N): # 이전꺼 + 현재꺼가 이전거보다 더 크면 이전거 + 현재거 아니면 현재거
    if lst[i] + dp[i-1] > lst[i]:
        dp[i] = lst[i] + dp[i-1]
    else:
        dp[i] = lst[i]
print(max(dp))

