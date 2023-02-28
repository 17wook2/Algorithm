from collections import deque
import math
n,m = list(map(int,input().split()))
arr = []
sh = []
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] == 1:
            sh.append((i,j))
    arr.append(row)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
dist = [[math.inf]*m for i in range(n)]

def go(x,y):
    q = deque()
    q.append((x,y))
    visited = [[0]*m for i in range(n)]
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if arr[nx][ny]: continue
            if visited[nx][ny]: continue
            visited[nx][ny] = visited[x][y] + 1
            dist[nx][ny] = min(dist[nx][ny], visited[nx][ny])
            q.append((nx,ny))

for s in sh:
    x,y = s
    go(x,y)
ans = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] == math.inf: continue
        ans = max(ans,dist[i][j])
print(ans)