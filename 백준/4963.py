# 1030
from collections import deque
while True:
    w,h = list(map(int,input().split()))
    if w == 0 and h == 0:
        break
    arr = []
    for i in range(h):
        arr.append(list(map(int,input().split())))
    cnt = 0
    visited = [[0]*w for i in range(h)]
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    q = deque()
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == 1:
                cnt += 1
                visited[i][j] = cnt
                q.append((i,j))
                while q:
                    x,y = q.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and arr[nx][ny] == 1:
                            visited[nx][ny] = cnt
                            q.append((nx,ny))
    print(cnt)



