from collections import deque
import math
def isPossible(x,y):
    if x < 0 or x >= r or y < 0 or y >= c:
        return True
    return False

def bfs():
    while q:
        x,y,cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isPossible(nx,ny) and arr[x][y] == '@':
                return cnt + 1
            elif 0 <= nx < r and 0 <= ny < c:
                if arr[x][y] == '@' and arr[nx][ny] == '.':
                    arr[nx][ny] = '@'
                    q.append((nx,ny,cnt+1))
                elif arr[x][y] == '*' and (arr[nx][ny] == '.' or arr[nx][ny] == '@'):
                    arr[nx][ny] = '*'
                    q.append((nx,ny,-1))
    return math.inf

t = int(input())
for _ in range(t):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    c,r = map(int,input().split())
    arr = []
    q = deque([])
    visited = [[0]*c for i in range(r)]
    start = []; fire = [];
    for i in range(r):
        lst = list(input())
        for j in range(c):
            if lst[j] == '@':
                start.append((i,j,0))
            elif lst[j] == '*':
                fire.append((i,j,-1))
        arr.append(lst)
    for node in start:
        q.append(node)
    for node in fire:
        q.append(node)
    ans = bfs()
    if ans == math.inf:
        print("IMPOSSIBLE")
    else:
        print(ans)


