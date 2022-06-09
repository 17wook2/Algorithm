from collections import deque
def change_direction(d):
    if d == 1:
        return 1
    elif d == 2:
        return 3
    elif d == 3:
        return 2
    elif d == 4:
        return 0

def bfs():
    q = deque([])
    q.append((sx,sy,sd))
    visited[sx][sy][sd] = 0
    while q:
        x,y,d = q.popleft()
        # print(x,y,d)
        if x == des_x and y == des_y and d == des_d:
            return visited[x][y][d]
        for i in range(1,4):
            nx = x + dx[d]*i
            ny = y + dy[d]*i
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    break
                if visited[nx][ny][d] == -1:
                    visited[nx][ny][d] = visited[x][y][d] + 1
                    q.append((nx,ny,d))
        for k in [-1,1]:
            nd = (d+k) % 4
            if visited[x][y][nd] == -1:
                visited[x][y][nd] = visited[x][y][d] + 1
                q.append((x,y,nd))

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
sx,sy,sd = list(map(int,input().split()))
sx-= 1; sy -=1;
sd = change_direction(sd)
des_x,des_y,des_d = list(map(int,input().split()))
des_x-=1; des_y-=1;
des_d = change_direction(des_d)
visited = [[[-1]*4 for i in range(m)] for i in range(n)]

print(bfs())
# for row in visited:
#     print(row)