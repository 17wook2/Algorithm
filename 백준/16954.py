from collections import deque
arr = []
wall = []
for i in range(8):
    row = list(input())
    for j in range(8):
        if row[j] == '#':
            wall.append((i,j))
    arr.append(row)
wall.sort(key = lambda x:-x[0])
visited = [[0]*8 for i in range(8)]
queue = deque([])
queue.append((7,0))
dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]
ans = 0
while queue:
    visited = [[0] * 8 for i in range(8)]
    for _ in range(len(queue)):
        x,y = queue.popleft()
        visited[x][y] = 1
        if arr[x][y] == '#':
            continue
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 8 and 0 <= ny < 8 and arr[nx][ny] != '#' and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))
        queue.append((x,y))
    new_wall = []
    for i in range(len(wall)):
        wx,wy = wall[i]
        if wx != 7:
            new_wall.append((wx+1,wy))
            arr[wx+1][wy] = '#'
            arr[wx][wy] = '.'
        else:
            arr[wx][wy] = '.'
    if len(new_wall) == 0:
        if len(queue) > 0:
            ans = 1
        else:
            ans = 0
        break
    wall.clear()
    for new in new_wall:
        wall.append(new)
print(ans)