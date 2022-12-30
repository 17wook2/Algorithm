from collections import deque
import math
def go(start,end):
    cnt = 0
    visited = [[0]*(m+1) for i in range(n+1)]
    x,y = start
    cnt += bfs(x,y,visited)
    x,y = end
    cnt += bfs(x,y,visited)
    return cnt
def bfs(a,b,visited):
    temp = [[0]*(m+1) for i in range(n+1)]
    q = deque([])
    q.append((a,b,[(a,b)]))
    temp[a][b] = 1
    k = arr[a][b]
    while q:
        x,y,route = q.popleft()
        if not(a == x and b == y) and arr[x][y] == arr[a][b]:
            for node in route:
                visited[node[0]][node[1]] = 1
            return len(route) - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n and 0 <= ny <= m and not temp[nx][ny] and arr[nx][ny] != -k and not visited[nx][ny]:
                temp[nx][ny] = 1
                new_route = route[:]
                new_route.append((nx,ny))
                q.append((nx,ny,new_route))
    return math.inf


m,n = list(map(int,input().split()))
arr = [[0]*(m+1) for i in range(n+1)]
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
b1 = list(map(int,input().split()))
b2 = list(map(int,input().split()))
arr[a1[1]][a1[0]] = 1
start = (a1[1],a1[0])
arr[a2[1]][a2[0]] = 1
arr[b1[1]][b1[0]] = -1
end = (b1[1], b1[0])
arr[b2[1]][b2[0]] = -1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = math.inf

ans = min(ans,go(start,end))
ans = min(ans,go(end,start))

if ans == math.inf:
    print("IMPOSSIBLE")
else:
    print(ans)