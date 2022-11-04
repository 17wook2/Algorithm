import math
from collections import deque
r,c = list(map(int,input().split()))
start = []
fire = []
arr = []
dx = [-1,0,1,0]; dy = [0,1,0,-1];
def check(x,y):
    if x == 0 or x == r-1 or y == 0 or y == c-1:
        return True
    else:
        return False

def simulate():
    q = deque([])
    x,y = start[0]
    q.append((x,y,0))
    for f in fire:
        fx,fy = f
        q.append((fx,fy,-1))
    while q:
        x,y,t = q.popleft()
        if check(x,y) and t > -1 and arr[x][y] != 'F':
            return t + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != '#':
                if t == -1 and arr[nx][ny] != 'F':
                    arr[nx][ny] = 'F'
                    q.append((nx,ny,-1))
                elif t > -1 and arr[nx][ny] == '.':
                    arr[nx][ny] = '_'
                    q.append((nx,ny,t+1))
    return -1

for i in range(r):
    lst = list(input())
    for j in range(c):
        if lst[j] == 'J':
            start.append((i,j))
        elif lst[j] == 'F':
            fire.append((i,j))
    arr.append(lst)

res = simulate()
if res == -1:
    print("IMPOSSIBLE")
else:
    print(res)