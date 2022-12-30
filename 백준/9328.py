from collections import deque
def bfs():
    q = deque([])
    q.append((0,0))
    visited = [[0] * (c+2) for i in range(r+2)]
    visited[0][0] = 1
    new_keys = []
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r+2 and 0 <= ny < c+2 and arr[nx][ny] != '*' and not visited[nx][ny]:
                if arr[nx][ny] == '.':
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                elif arr[nx][ny] == '$':
                    visited[nx][ny] = 1
                    cnt += 1
                    q.append((nx,ny))
                elif 65 <= ord(arr[nx][ny]) <= 90: ## 문인경우
                    k = chr(ord(arr[nx][ny]) + 32)
                    if k in keys:
                        visited[nx][ny] = 1
                        q.append((nx,ny))
                elif 97 <= ord(arr[nx][ny]) <= 122:
                    k = arr[nx][ny]
                    if k in keys:
                        visited[nx][ny] = 1
                        q.append((nx,ny))
                    else:
                        new_keys.append(k)
                        keys.append(k)
                        visited[nx][ny] = 1
                        q.append((nx,ny))
    if len(new_keys) == 0:
        return [-1,cnt]
    else:
        return [1,cnt]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
t = int(input())
for _ in range(t):
    r,c = map(int,input().split())
    arr = []
    arr.append(['.' for i in range(c+2)])
    for i in range(r):
        x = ['.']
        x.extend(list(input()))
        x.append('.')
        arr.append(x)
    arr.append(['.' for i in range(c+2)])
    str = input()
    keys = []
    if str != '0':
        for x in str: keys.append(x)
    ans = 0
    while True:
        f,cnt = bfs()
        ans = max(ans,cnt)
        if f == -1:
            break
    print(ans)


