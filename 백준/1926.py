from collections import deque, Counter
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
visited = [[0]*(m) for i in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs():
    cnt = 0
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                queue.append((i,j))
                cnt += 1
                visited[i][j] = cnt
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                            visited[nx][ny] = cnt
                            queue.append((nx,ny))
    print(cnt)
bfs()
a = Counter([])
for row in visited:
    counter = Counter(row)
    a += counter
if len(a) == 1:
    if a.most_common()[0][0] == 0:
        print(0)
    else:
        print(a.most_common()[0][1])
else:
    if a.most_common()[0][0] == 0:
        print(a.most_common()[1][1])
    else:
        print(a.most_common()[0][1])