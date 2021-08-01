from itertools import combinations
from collections import deque
import copy
import math
n,m = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

virus = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i,j))

combi = list(combinations(virus,m))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(array):
    for i in range(n):
        for j in range(n):
            if array[i][j] == 0:
                return False
    return True

def simulation(aarr,c):
    visited = [[0 for i in range(n)] for i in range(n)]
    queue = deque([])
    for location in c:
        x,y = location
        queue.append((x,y,0))
    rtn = 0
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and aarr[nx][ny] != 1:
                visited[nx][ny] = 1
                if aarr[nx][ny] == 0:
                    aarr[nx][ny] = 2
                    rtn = cnt + 1
                queue.append((nx,ny,cnt+1))

    if check(aarr): ## 0이 없는것
        return rtn
    else:
        return -1


answer = math.inf
for comb in combi:
    array = copy.deepcopy(arr)
    k = simulation(array,comb)
    if k == -1:
        continue
    else:
        answer = min(answer,k)

if answer == math.inf:
    print(-1)
else:
    print(answer)

