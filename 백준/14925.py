import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
dp = [[0]*(m+1) for i in range(n+1)]
for i in range(n):
    x = list(map(int,input().split()))
    arr.append(x)
for i in range(1,n+1):
    for j in range(1,m+1):
        if not arr[i-1][j-1]:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
ans = 0
for row in dp:
    print(row)
    ans = max(ans,max(row))
print(ans)

