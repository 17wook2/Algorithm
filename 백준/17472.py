from collections import deque
def bfs():
    cnt = 1
    for i in range(n):
        for j in range(m):
            if not land[i][j] and arr[i][j]:
                land[i][j] = cnt
                cnt += 1
                q = deque([])
                q.append((i,j))
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and not land[nx][ny] and arr[nx][ny]:
                            land[nx][ny] = land[x][y]
                            q.append((nx,ny))
    return cnt-1

def connect(x,y,d):
    move = 1
    target = land[x][y]
    while True:
        x = x + dx[d]
        y = y + dy[d]
        if x < 0 or x >= n or y < 0 or y >= m: return -1,-1
        if land[x][y] == target: return -1,-1
        if land[x][y] == 0: move += 1; continue
        if land[x][y] != target: return move-1,land[x][y]

def make_graph():
    for x in range(n):
        for y in range(m):
            if land[x][y] != 0:
                for k in range(4):
                    a = land[x][y]
                    move, b = connect(x,y,k)
                    if move <= 1: continue
                    edges.append((move,a,b))

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
def kruskal():
    ans = 0
    cnt = 0
    for edge in edges:
        move,a,b = edge
        if find(a) != find(b):
            union(a,b)
            ans += move
            cnt += 1
    return ans,cnt

def go():
    cnt = bfs()
    make_graph()
    edges.sort()
    ans,edge = kruskal()
    if edge == cnt-1:
        return ans
    else:
        return -1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = list(map(int,input().split()))
arr = []
land = [[0]*m for i in range(n)]
edges = []
parents = [0]*10
for i in range(10):
    parents[i] = i
for i in range(n):
    arr.append(list(map(int,input().split())))
print(go())

