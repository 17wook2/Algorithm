from collections import deque
import math
n,m = list(map(int,input().split()))
arr = []
dist = [[[math.inf,math.inf] for i in range(m)] for i in range(n)]
for i in range(n):
    x = list(input())
    temp = []
    for j in range(m):
        if x[j] == '/': temp.append(1)
        else: temp.append(0)
    arr.append(temp)
q = deque([])
if arr[0][0] == 1: dist[0][0][0] = 1
else: dist[0][0][0] = 0

q.append((0,0,0))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ddx = [-1,1,-1,1]
ddy = [-1,1,1,-1]
while q:
    x,y,d = q.popleft()
    cost = dist[x][y][d]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if d == arr[nx][ny]: ## 방향 같으면 스위칭
                nd = d ^ 1
                if cost + 1 >= dist[nx][ny][nd]: continue
                dist[nx][ny][nd] = cost + 1
                q.append((nx,ny,nd))
            else: ## 방향 다른 경우 큐 앞에 삽입
                nd = d ^ 1
                if cost >= dist[nx][ny][nd]: continue
                dist[nx][ny][nd] = cost
                q.appendleft((nx,ny,nd))
    for i in range(4): ## 대각선
        nx = x + ddx[i]
        ny = y + ddy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if d == 0 and i >= 2: continue
            if d == 1 and i < 2: continue
            if d != arr[nx][ny]:
                nd = d
                if cost + 1 >= dist[nx][ny][nd]: continue
                dist[nx][ny][nd] = cost + 1
                q.append((nx,ny,nd))
            elif d == arr[nx][ny]:
                if cost >= dist[nx][ny][d]: continue
                dist[nx][ny][d] = cost
                q.appendleft((nx,ny,d))

if dist[n-1][m-1][0] == math.inf:
    print("NO SOLUTION")
else:
    print(dist[n-1][m-1][0])



