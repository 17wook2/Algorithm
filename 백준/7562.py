from collections import deque
t = int(input())
def bfs():
    q = deque()
    q.append((sx,sy,0))
    visited = [[0]*n for i in range(n)]
    while q:
        x,y,cnt = q.popleft()
        if x == ex and y == ey:
            return cnt
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if visited[nx][ny]: continue
            visited[nx][ny] = 1
            q.append((nx,ny,cnt+1))

for _ in range(t):
    n = int(input())
    sx,sy = list(map(int,input().split()))
    ex,ey = list(map(int,input().split()))
    dp = [[0]*n for i in range(n)]
    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]
    cnt = bfs()
    print(cnt)
