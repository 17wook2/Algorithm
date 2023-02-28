from collections import deque
n,m = list(map(int,input().split()))
arr = []
ans = [[-1]*m for i in range(n)]
visited = [[0]*m for i in range(n)]
sx,sy = 0,0;
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] == 2:
            sx = i; sy = j
        if row[j] == 0:
            ans[i][j] = 0
    arr.append(row)
q = deque()
q.append((sx,sy))
ans[sx][sy] = 0
visited[sx][sy] = 1
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
            ans[nx][ny] = ans[x][y] + 1
            visited[nx][ny] = 1
            q.append((nx,ny))
for row in ans:
    print(*row)
