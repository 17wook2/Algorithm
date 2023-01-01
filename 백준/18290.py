import math
n,m,k = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
visited = [[0]*m for i in range(n)]
ans = -math.inf
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def go():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 1
            for idx in range(4):
                nx = i + dx[idx]
                ny = j + dy[idx]
                if 0 <= nx < n and 0 <= ny < m:
                    visited[nx][ny] = 1
            dfs(1,arr[i][j],i,j)
            for x in range(n):
                for y in range(m):
                    visited[x][y] = 0
def dfs(cnt,total,cx,cy):
    global ans
    if cnt == k:
        ans = max(ans, total)
        return
    for i in range(cx,n):
        for j in range(m):
            if visited[i][j] == 1: continue
            checked = []
            checked.append((i,j))
            visited[i][j] = 1
            for _ in range(4):
                nx = i + dx[_]
                ny = j + dy[_]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    checked.append((nx,ny))
            dfs(cnt+1, total + arr[i][j],i,j)
            for x,y in checked:
                visited[x][y] = 0

go()
print(ans)