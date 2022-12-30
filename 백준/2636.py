from collections import deque
r,c = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs():
    temp = [[0]*c for i in range(r)]
    visited = [[0]*c for i in range(r)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] == 1:
                    temp[nx][ny] = 1
                elif arr[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    cnt, blow = 0,0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                cnt += 1
            if temp[i][j] == 1:
                blow += 1
                arr[i][j] = 0
    return cnt,cnt-blow

def check():
    res = 0
    for row in arr:
        res += sum(row)
    return res
arr = []
for i in range(r):
    arr.append(list(map(int,input().split())))
ans = 0
cnt = 0
while check():
    before,after = bfs()
    ans = before
    cnt += 1
print(cnt)
print(ans)


