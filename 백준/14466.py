from collections import deque
import math
n,k,r = list(map(int,input().split()))
road = [[[0]*4 for i in range(n+1)] for i in range(n+1)]
cow = []
farm = [[0]*(n+1) for i in range(n+1)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def mark(r,c,a,b):
    for i in range(4):
        if a == dx[i] and b == dy[i]:
            road[r][c][i] = 1

def bfs(x,y):
    queue = deque([])
    queue.append((x,y))
    visited = [[0]*(n+1) for i in range(n+1)]
    visited[x][y] = 1
    cnt = 0
    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx <= n and 0 < ny <= n and not visited[nx][ny] and not road[x][y][i]:
                visited[nx][ny] = 1
                if farm[nx][ny] == 1:
                    cnt += 1
                queue.append((nx,ny))
    return cnt
for i in range(r):
    r1,c1,r2,c2 = list(map(int,input().split()))
    mark(r1,c1,r2-r1,c2-c1)
    mark(r2,c2,r1-r2,c1-c2)

for i in range(k):
    x,y = list(map(int,input().split()))
    farm[x][y] = 1
    cow.append((x,y))

f = math.factorial(k) / math.factorial(k-2)
f = int(f)
cnt = 0
for i in range(len(cow)):
    cnt += bfs(cow[i][0],cow[i][1])

ans = (f-cnt) / 2
ans = int(ans)
print(ans)

