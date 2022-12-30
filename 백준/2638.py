from collections import deque
def bfs():
    q = deque([])
    visited = [[0]*c for i in range(r)]
    temp = [[0]*c for i in range(r)]
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] == 1:
                    cnt = 0
                    for k in range(4):
                        nnx = nx + dx[k]
                        nny = ny + dy[k]
                        if arr[nnx][nny] == 0 and visited[nnx][nny]:
                            cnt += 1
                    if cnt >= 2:
                        temp[nx][ny] = 1
                elif arr[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))

    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1 and temp[i][j] == 1:
                arr[i][j] = 0

def check():
    res = 0
    for row in arr:
        res += sum(row)
    return res

dx = [-1,0,1,0]
dy = [0,1,0,-1]
r,c = map(int,input().split())
arr = []
for i in range(r):
    arr.append(list(map(int,input().split())))
ans = 0

while check():
    bfs()
    ans += 1
print(ans)