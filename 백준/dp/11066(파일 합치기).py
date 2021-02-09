import math
T = int(input())
for _ in range(T):
    n = int(input())
    files = list(map(int,input().split()))
    # print(files)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for j in range(1,n):
        for i in range(j-1,-1,-1):
            small = math.inf
            for k in range(j-i): # k는 횟수
                small = min(small, dp[i][i+k]+dp[i+k+1][j])
            dp[i][j] = small + sum(files[i:j+1])
    print(dp[0][n-1])
