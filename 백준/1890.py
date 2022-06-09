n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
ans = 0
dx = [0,1]
dy = [1,0]
dp = [[-1]*n for i in range(n)]
def dfs(x,y):
    global ans
    if x == n-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(2):
        nx = x + dx[i]*arr[x][y]
        ny = y + dy[i]*arr[x][y]
        if 0 <= nx < n and 0 <= ny < n and arr[x][y] > 0:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]
dfs(0,0)
print(dp[0][0])

