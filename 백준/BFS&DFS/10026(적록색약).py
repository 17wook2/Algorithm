from collections import deque
n = int(input())
maps = [list(input()) for i in range(n)]
# print(maps)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs():
    visited = [[0]*(n+1) for i in range(n+1)]
    queue = deque([])
    queue.append((0,0))
    idx = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] != 0:
                continue
            else:
                idx += 1
                queue.append((i,j))
                while queue:
                    x,y = queue.popleft()
                    visited[x][y] = idx
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                            if maps[nx][ny] == maps[x][y]:
                                visited[nx][ny] = idx
                                queue.append((nx,ny))
    # print(visited)
    return idx

def b_bfs():
    visited = [[0]*(n+1) for i in range(n+1)]
    queue = deque([])
    queue.append((0,0))
    idx = 0
    color = ['R','G']
    for i in range(n):
        for j in range(n):
            if visited[i][j] != 0:
                continue
            else:
                idx += 1
                queue.append((i,j))
                while queue:
                    x,y = queue.popleft()
                    visited[x][y] = idx
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                            if maps[nx][ny] == maps[x][y] or (maps[nx][ny] in color and maps[x][y] in color):
                                visited[nx][ny] = idx
                                queue.append((nx,ny))
    return idx

print(bfs(),b_bfs())