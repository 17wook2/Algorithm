from collections import deque
r,c = map(int,input().split())
arr = []
for i in range(r):
    arr.append(list(input()))
n = int(input())
heights = list(map(int,input().split()))
turn = 1 ## 왼쪽턴
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def move(cluster,visited):
    cnt = 1; t = 0
    while True:
        for mineral in cluster:
            mx,my = mineral
            if mx + cnt == r-1:
                t = 1
                break
            if arr[mx+cnt+1][my] == 'x' and not visited[mx+cnt+1][my]:
                t = 1
                break
        if t:
            break
        cnt += 1
    for i in range(r-2,-1,-1):
        for j in range(c):
            if arr[i][j] == 'x' and visited[i][j]:
                arr[i][j] = '.'
                arr[i+cnt][j] = 'x'



def bfs(x,y):
    visited = [[0 for i in range(c)] for i in range(r)]
    cluster = []
    if arr[x][y] != 'x':
        return
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        cluster.append((x,y))
        if x == r-1:
            return
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and arr[nx][ny] == 'x':
                visited[nx][ny] = 1
                queue.append((nx,ny))
    move(cluster,visited)

for h in heights:
    queue = deque([])
    if turn:
        for i in range(c):
            if arr[r-h][i] == 'x':
                arr[r-h][i] = '.'
                for k in range(4):
                    nx = r-h + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < r and 0 <= ny < c:
                        queue.append((nx,ny))
                break
        turn = 0
    else:
        for i in range(c-1,-1,-1):
            if arr[r-h][i] == 'x':
                arr[r-h][i] = '.'
                for k in range(4):
                    nx = r-h + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < r and 0 <= ny < c:
                        queue.append((nx,ny))
                break
        turn = 1
    while queue:
        x,y = queue.popleft()
        bfs(x,y)
for row in arr:
    print(''.join(row))