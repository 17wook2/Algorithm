import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(input()))
visited = [[0]*m for i in range(n)]
dp = [[-1]*m for i in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m or arr[x][y] == 'H':
        return 0
    if visited[x][y]:
        print(-1)
        exit(0)
    if dp[x][y] != -1:
        return dp[x][y]
    visited[x][y] = 1
    dp[x][y] = 0
    d = int(arr[x][y])
    for i in range(4):
        nx = x + dx[i]*d
        ny = y + dy[i]*d
        dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)
    visited[x][y] = 0
    return dp[x][y]

print(dfs(0,0))
