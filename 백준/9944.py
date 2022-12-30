import sys
import math
sys.setrecursionlimit(10**9)
def end_check():
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.' and not visited[i][j]:
                return False
    return True

def oob_check(x,y):
    if 0 <= x < r and 0 <= y < c and arr[x][y] != '*' and not visited[x][y]:
        return True
    return False

def move(x,y,d):
    visited[x][y] = 1
    while True:
        x = x + dx[d]
        y = y + dy[d]
        if oob_check(x,y): visited[x][y] = 1
        else: return x-dx[d], y-dy[d]
def remove(x,y,nx,ny,d):
    visited[x][y] = 0
    while True:
        if x == nx and y == ny:
            visited[x][y] = 0
            return
        else:
            x = x + dx[d]
            y = y + dy[d]
            visited[x][y] = 0
    return

def dfs(x,y,cnt):
    global ans
    if cnt >= ans:
        return
    is_finished = True;
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if oob_check(nx,ny):
            is_finished = False
            nnx, nny = move(nx,ny,i)
            dfs(nnx,nny,cnt+1)
            remove(nx,ny,nnx,nny,i)
    if is_finished:
        if end_check():
            ans = min(ans,cnt)
            return
tc = 1
while True:
    try:
        dx = [-1,0,1,0]; dy = [0,1,0,-1]
        r,c = list(map(int,input().split()))
        arr = []
        ans = math.inf
        visited = [[0]*c for i in range(r)]
        for i in range(r):
            arr.append(list(input()))
        for i in range(r):
            for j in range(c):
                if arr[i][j] == '.':
                    visited[i][j] = 1
                    dfs(i,j,0)
                    visited[i][j] = 0
        if ans == math.inf:
            ans = -1
        print(f"Case {tc}: {ans}")
        tc += 1;
    except:
        break