from collections import deque
def matching(x,y):
    visited = [[0 for i in range(n)] for i in range(n)]
    visited[x][y] = 1
    queue = deque([])
    queue.append((x,y,0))
    candidate = []
    while queue:
        x,y,distance = queue.popleft()
        if arr[x][y] >= 2:
            candidate.append((x,y,distance))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny,distance+1))
    if len(candidate) > 0:
        candidate.sort(key = lambda x: (x[2],x[0],x[1]))
        return candidate[0]
    return (0,0,-1)
def destination(a,b,x,y):
    visited = [[0 for i in range(n)] for i in range(n)]
    queue = deque([])
    queue.append((a,b,0))
    visited[a][b] = 1
    while queue:
        a,b,d = queue.popleft()
        if a == x and b == y:
            return d
        else:
            for i in range(4):
                na = a + dx[i]
                nb = b + dy[i]
                if 0 <= na < n and 0 <= nb < n and not visited[na][nb] and arr[na][nb] != 1:
                    queue.append((na,nb,d+1))
                    visited[na][nb] = 1
    return -1
n,m,fuel= list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
start = list(map(int,input().split()))
start = list(map(lambda x:x-1, start))
drive = []
for i in range(m):
    p = list(map(int,input().split()))
    p = list(map(lambda x: x-1, p))
    arr[p[0]][p[1]] = i+2
    drive.append(p)
dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt = 0

for i in range(m):
    a,b,d = matching(start[0],start[1])
    if d > fuel or d == -1:
        break
    else:
        fuel -= d

    des_a = drive[arr[a][b]-2][2]
    des_b = drive[arr[a][b]-2][3]
    dd = destination(a,b,des_a, des_b)
    arr[a][b] = 0
    if dd > fuel or dd == -1:
        break
    else:
        fuel -= dd
        cnt += 1
    fuel += 2*dd
    start[0],start[1] = des_a, des_b

if cnt < m:
    print(-1)
else:
    print(fuel)