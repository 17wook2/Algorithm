from collections import deque
m,n = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def go():
    visited = [[0]*m for i in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i, j))
                visited[i][j] = 1
    time = 0
    while q:
        q_len = len(q)
        while q_len:
            q_len -= 1
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] != -1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
        time += 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] != -1 and visited[i][j] == 0:
                time = -1
                return time
    return time-1

print(go())

