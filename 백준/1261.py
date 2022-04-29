from collections import deque
m,n = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
arr = []
visited = [[0]*m for i in range(n)]
for i in range(n):
    arr.append(list(map(int,input())))
def bfs():
    queue = deque([])
    queue.append((0,0,0))
    visited[0][0] = 1
    while queue:
        x,y,cnt = queue.popleft()
        if x == n-1 and y == m-1:
            print(cnt)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if arr[nx][ny] == 0:
                    queue.appendleft((nx,ny,cnt))
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    queue.append((nx,ny,cnt+1))
bfs()
