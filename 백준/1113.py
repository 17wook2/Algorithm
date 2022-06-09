from collections import deque
n,m = map(int,input().split())
arr = []
max_height = 0
min_height = 99
for i in range(n):
    x = list(map(int,input()))
    max_height = max(max_height,max(x))
    min_height = min(min_height, min(x))
    arr.append(x)
dx = [-1,0,1,0]
dy = [0,1,0,-1]
water = [[0]*m for i in range(n)]

def bfs(x,y,h,visited):
    q = deque([])
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        water[x][y] -= 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny]:
                continue
            if nx == 0 or nx == n-1 or ny == 0 or ny == m-1:
                continue
            if water[nx][ny] and arr[nx][ny] + water[nx][ny] == h:
                visited[nx][ny] = 1
                q.append((nx,ny))

def solve():
    for i in range(1,n-1):
        for j in range(1,m-1):
            water[i][j] = max_height - arr[i][j]
    for h in range(max_height,1,-1):
        visited = [[0] * m for i in range(n)]
        for i in range(1,n-1):
            for j in range(1,m-1):
                if water[i][j] and not visited[i][j]:
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if water[i][j] + arr[i][j] > water[nx][ny] + arr[nx][ny]:
                            bfs(i,j,h,visited)
                            break
        # for row in water:
        #     print(row)
        # print()
solve()
ans = 0
for i in range(1,n-1):
    for j in range(1,m-1):
        ans += water[i][j]
print(ans)

