from collections import deque
import math
def bfs():
    a,b = lights[0]
    aa,bb = lights[1]
    q = deque([])
    q.append((a,b))
    visited[a][b] = -1
    while q:
        x,y = q.popleft()
        if x == aa and y == bb:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if not (0 <= nx < r and 0 <= ny < c): break
                if arr[nx][ny] == '*': break
                if visited[nx][ny] < visited[x][y] + 1: break
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                nx += dx[i]; ny += dy[i];





    return visited[aa][bb]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
c,r = map(int,input().split())
arr = []
lights = []
visited = [[math.inf]*c for i in range(r)]
for i in range(r):
    lst = list(input())
    for j in range(c):
        if lst[j] == 'C': lights.append((i,j))
    arr.append(lst)

print(bfs())
