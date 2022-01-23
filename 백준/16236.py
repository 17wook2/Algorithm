from collections import deque
import math
n = int(input())
arr = []
for i in range(n):
    tmp = list(map(int,input().split()))
    arr.append(tmp)
shark_x = 0
shark_y = 0
shark_weight = 2
ans = 0
fish_cnt = 0
st = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark_x = i
            shark_y = j
            arr[i][j] = 0
        if 0 < arr[i][j] <= 6:
            fish_cnt += 1

def bfs(sx,sy):
    queue = deque([])
    queue.append((sx,sy,0))
    visited = [[0]*n for i in range(n)]
    visited[sx][sy] = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    mdist = math.inf
    flist = []
    while queue:
        # print(queue)
        x,y,d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] <= shark_weight:
                visited[nx][ny] = 1
                if 0 < arr[nx][ny] < shark_weight:
                    mdist = d + 1
                    flist.append((mdist, nx, ny))
                if d < mdist:
                    queue.append((nx,ny,d+1))


    flist.sort()
    if len(flist) == 0:
        return (-1,-1,-1)
    else:
        return (flist[0][0],flist[0][1],flist[0][2])

while fish_cnt:
    d,x,y = bfs(shark_x,shark_y)
    if x == -1 and y == -1:
        break
    # fish 잡아 먹힌경우
    st += 1
    if st == shark_weight:
        st = 0
        shark_weight += 1
    shark_x = x
    shark_y = y
    arr[shark_x][shark_y] = 0
    ans += d
    fish_cnt -= 1

print(ans)
