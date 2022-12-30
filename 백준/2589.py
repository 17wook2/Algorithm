from collections import deque
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited = [[-1]*c for i in range(r)]
    visited[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == -1 and arr[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    res = 0
    for i in range(r):
        for j in range(c):
            res = max(res,visited[i][j])
    return res

dx = [-1,0,1,0]
dy = [0,1,0,-1]
r,c = map(int,input().split())
arr = []
ans = 0
for i in range(r):
    arr.append(list(input()))
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            ans = max(ans,bfs(i,j))
print(ans)
