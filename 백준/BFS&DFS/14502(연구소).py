from itertools import combinations
from collections import deque
import copy
n,m = list(map(int,input().split()))
lab = [list(map(int,input().split())) for i in range(n)]
# 벽 3개
virus = []
empty = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
answer = 0
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus.append((i,j))
        elif lab[i][j] == 0:
            empty.append((i,j))
def safeaarea(candidates):
    new_lab = copy.deepcopy(lab)
    queue = deque()
    for v in virus:
        queue.append(v)
    area = 0
    for cands in candidates:
        new_lab[cands[0]][cands[1]] += 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m and new_lab[nx][ny] == 0:
                new_lab[nx][ny] = 2
                queue.append((nx,ny))
    for row in new_lab:
        for column in row:
            if column == 0:
                area += 1
    return area
candidate = combinations(empty,3)
for cand in candidate:
    answer = max(answer, safeaarea(cand))
    # print(answer)
print(answer)


