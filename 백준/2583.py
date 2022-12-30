from collections import deque
def bfs(x,y):
    q =deque([])
    q.append((x,y))
    cnt = 0
    while q:
        x,y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))
    return cnt

dx = [-1,0,1,0]
dy = [0,1,0,-1]
c,r,k = map(int,input().split())
arr = [[0]*c for i in range(r)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x2-x1):
        for j in range(y2-y1):
            arr[x1+i][y1+j] = 1
visited = [[0]*c for i in range(r)]
ans = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = 1
            ans.append(bfs(i,j))

print(len(ans))
ans.sort()
print(*ans)

