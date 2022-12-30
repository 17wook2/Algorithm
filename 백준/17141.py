from itertools import combinations
from collections import deque
import math
n,m = list(map(int,input().split()))
arr = []
candidate = []
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        if temp[j] == 2:
            candidate.append((i,j))
    arr.append(temp)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(c1):
    q = deque()
    visited = [[-1]*n for i in range(n)]
    for c in c1:
        x,y = candidate[c]
        q.append((x,y))
        visited[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if arr[nx][ny] == 1: continue
            if visited[nx][ny] != -1: continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))
    move = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1: continue
            if visited[i][j] == -1: return math.inf
            move = max(move,visited[i][j])
    return move

def go():
    ans = math.inf
    for c1 in combinations(range(len(candidate)),m):
        ans = min(ans, bfs(c1))
    if ans == math.inf:
        return -1
    return ans

print(go())