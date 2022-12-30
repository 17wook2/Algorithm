from collections import deque
tc = int(input())
def bfs(sx,sy,ex,ey):
    q = deque([])
    q.append((sx,sy))
    visited = [[-1]*n for i in range(n)]
    visited[sx][sy] = 0
    while q:
        x,y = q.popleft()
        if x == ex and y == ey:
           print(visited[ex][ey])
           return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))


for _ in range(tc):
    n = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]
    bfs(start[0],start[1],end[0],end[1])