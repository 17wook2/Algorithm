import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
m = int(input())
dp = [[0]*n for i in range(n)]
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
for i in range(n-1,-1,-1):
    for j in range(i+2,n,1):
        if arr[i] == arr[j] and dp[i+1][j-1]:
            dp[i][j] = 1
for i in range(m):
    s,e = map(int,input().split())
    s -= 1; e -= 1;
    print(dp[s][e])
