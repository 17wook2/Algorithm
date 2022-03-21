import sys
input = sys.stdin.readline
n,m,k = list(map(int,input().strip().split()))
arr = []
for i in range(n):
    row = list(input().strip())
    arr.append(row)
cmp = list(input().strip())
start = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == cmp[0]:
            start.append((i,j))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
dp = [[[-1]*len(cmp) for i in range(m)] for i in range(n)]
ans = 0
def dfs(x,y,depth):
    global ans
    if dp[x][y][depth] != -1:
        return dp[x][y][depth]
    if depth == len(cmp)-1:
        return 1
    dp[x][y][depth] = 0
    for i in range(1,k+1):
        for j in range(4):
            nx = x + i * dx[j]
            ny = y + i * dy[j]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == cmp[depth+1]:
                    dp[x][y][depth] += dfs(nx,ny,depth+1)
    return dp[x][y][depth]

for st in start:
    x,y = st
    ans += dfs(x,y,0)
print(ans)