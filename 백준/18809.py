from collections import deque
from itertools import combinations
n,m,g,r = list(map(int,input().split()))
lake = []
spread = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(m):
        if temp[j] == 2:
            spread.append((i,j))
    lake.append(temp)
tot = len(spread)
bit = g + r
ans = 0

def bfs():
    ans = 0
    visited = [[[0, 0] for i in range(m)] for i in range(n)]
    q = deque()
    for i in selected_r:
        x,y = spread[i]
        visited[x][y][1] = 1
        q.append((x,y))
    for i in selected_g:
        x,y = spread[i]
        visited[x][y][1] = 2
        q.append((x,y))
    while q:
        x,y = q.popleft()
        if visited[x][y][1] == 3: continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if lake[nx][ny] == 0: continue
            if visited[nx][ny][1] == 0:
                visited[nx][ny][0] = visited[x][y][0] + 1
                visited[nx][ny][1] = visited[x][y][1]
                q.append((nx,ny))
            elif visited[nx][ny][1] == 1:
                if visited[x][y][1] == 2 and visited[nx][ny][0] == visited[x][y][0] + 1:
                    visited[nx][ny][1] = 3
                    ans += 1
            elif visited[nx][ny][1] == 2:
                if visited[x][y][1] == 1 and visited[nx][ny][0] == visited[x][y][0] + 1:
                    visited[nx][ny][1] = 3
                    ans += 1
    return ans

for c1 in combinations(range(len(spread)),g+r):
    for c2 in combinations(range(g+r), r):
        selected_r = []
        selected_g = []
        for i in range(r+g):
            if i in c2: selected_r.append(c1[i])
            else: selected_g.append(c1[i])
        ans = max(ans,bfs())
print(ans)
