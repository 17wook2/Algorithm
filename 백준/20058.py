from collections import deque
n,q = map(int,input().split())
n = 2**n
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
skills = list(map(int,input().split()))
ddx = [-1, 0, 1, 0]
ddy = [0, 1, 0, -1]
def do_magic(s,arr):
    r = 2**s
    new_arr = [[0]*n for i in range(n)]
    for x in range(0,n,r):
        for y in range(0,n,r):
            for j in range(r):
                for k in range(r):
                    new_arr[x+k][y+r-1-j] = arr[x+j][y+k]
    return new_arr

def calc():
    new_arr = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                continue
            cnt = 0
            for k in range(4):
                nx = i + ddx[k]
                ny = j + ddy[k]
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]: # 얼음과 인접합 칸
                    cnt += 1
            if cnt < 3:
                new_arr[i][j] = 1

    for i in range(n):
        for j in range(n):
            if new_arr[i][j]:
                arr[i][j] -= 1

def bfs():
    visited = [[0]*(n) for i in range(n)]
    rtn = 0
    queue = deque([])
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j]:
                queue.append((i,j))
                cnt = 0
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx = x + ddx[k]
                        ny = y + ddy[k]
                        if 0 <= nx <n and 0 <= ny <n and not visited[nx][ny] and arr[nx][ny]:
                            visited[nx][ny] = 1
                            queue.append((nx,ny))
                            cnt += 1
                rtn = max(rtn,cnt)
    return rtn

for s in skills:
    arr = do_magic(s,arr)
    calc()
ans = 0
for row in arr:
    ans += sum(row)
print(ans)
print(bfs())