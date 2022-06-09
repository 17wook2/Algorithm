import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
dp = [[-1]*m for i in range(n)]
def dfs(x,y):
    global ans
    if x == n-1 and y == m-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]
dfs(0,0)
# for row in dp:
#     print(row)
print(dp[0][0])