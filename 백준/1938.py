from collections import deque
n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))
b = []
e = []
for i in range(n):
    for j in range(n):
        if arr[i][j] =='B':
            b.append((i,j))
            arr[i][j] = '0'
        if arr[i][j] == 'E':
            e.append((i,j))
            arr[i][j] = '0'
def get_status(array):
    if array[0][0] == array[1][0]:
        d = 0 ## 누워있으면
    else:
        d = 1
    x = array[1][0]; y = array[1][1]
    return [x,y,d]
sx,sy,sd = get_status(b)
ex,ey,ed = get_status(e)
visited = [[[-1]*2 for i in range(n)] for i in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def check(x,y,d):
    for i in [-1,0,1]:
        if d == 1:
            nx = x + i
            ny = y
        elif d == 0:
            nx = x
            ny = y + i
        if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] == '1':
            return False
    return True

def bfs():
    q = deque([])
    q.append((sx,sy,sd))
    visited[sx][sy][sd] = 0
    while q:
        x,y,d = q.popleft()
        if x == ex and y == ey and d == ed:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny][d] != -1 or arr[nx][ny] == '1':
                continue
            if check(nx,ny,d):
                visited[nx][ny][d] = visited[x][y][d] + 1
                q.append((nx,ny,d))
        if visited[x][y][d^1] == -1:
            p = 1
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    nx = x + i
                    ny = y + j
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] == '1':
                        p = 0
            if p:
                visited[x][y][d^1] = visited[x][y][d] + 1
                q.append((x,y,d^1))

bfs()
ans = visited[ex][ey][ed]
if ans == -1:
    print(0)
else:
    print(ans)