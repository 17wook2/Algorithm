from collections import deque
n,m = map(int,input().split())
arr = []
walls = []
for i in range(n):
    row = list(map(int,input()))
    for j in range(len(row)):
        if row[j] == '1':
            walls.append((i,j))
    arr.append(row)

visited = [[0]*m for i in range(n)]
dp = [[0]*m for i in range(n)]
ans = [[0]*m for i in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            cnt += 1
            queue = deque([])
            queue.append((i,j))
            block = [(i,j)]
            while queue:
                x,y = queue.popleft()
                visited[x][y] = cnt
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 0:
                        visited[nx][ny] = cnt
                        block.append((nx,ny))
                        queue.append((nx,ny))
            length = len(block)
            for bl in block:
                bx,by = bl
                dp[bx][by] = length
for i in range(n):
    for j in range(m):
        appended = []
        if arr[i][j] == 0:
            continue
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] not in appended:
                appended.append(visited[nx][ny])
                ans[i][j] += dp[nx][ny]
        ans[i][j] += 1
        ans[i][j] %= 10
for row in ans:
    print(''.join(list(map(str,row))))