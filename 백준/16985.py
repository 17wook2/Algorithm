from collections import deque
from itertools import permutations
import math

def rotate(layer):
    rotated = []
    rotated.append(layer)
    for r in range(1,4):
        temp = [[0]*5 for i in range(5)]
        for i in range(5):
            for j in range(5):
                temp[i][j] = rotated[r-1][5-j-1][i]
        rotated.append(temp)
    return rotated
def oob(x,y,z):
    if x < 0 or x >= 5 or y < 0 or y >= 5 or z < 0 or z >= 5: return True
    return False
def bfs():
    q = deque([])
    visited = [[[-1 for i in range(5)] for i in range(5)] for i in range(5)]
    if simulate_array[0][0][0] == 0 or simulate_array[4][4][4] == 0: return math.inf
    visited[0][0][0] = 0
    q.append((0,0,0))
    while q:
        x,y,z = q.popleft()
        for i in range(6):
            nx = x + dx[i]; ny = y + dy[i]; nz = z + dz[i]
            if oob(nx,ny,nz): continue
            if visited[nx][ny][nz] != -1: continue
            if simulate_array[nx][ny][nz] == 0: continue
            if nx == 4 and ny == 4 and nz == 4: return visited[x][y][z] + 1;
            visited[nx][ny][nz] = visited[x][y][z] + 1
            q.append((nx,ny,nz))
    return math.inf

def go(order):
    ans = math.inf
    for total_bit in range(1<<10):
        cur_bit = total_bit
        for i in range(5):
            idx = (cur_bit & 3); cur_bit >>= 2
            for j in range(5):
                for k in range(5):
                    simulate_array[i][j][k] = cube[order[i]][idx][j][k]
        ans = min(ans,bfs())
    return ans

dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,-1,1]
simulate_array = [[[0 for i in range(5)] for i in range(5)] for i in range(5)]
cube = []
for i in range(5):
    layer = []
    for j in range(5):
        layer.append(list(map(int,input().split())))
    rotated = rotate(layer)
    cube.append(rotated)

stacking_order = list(permutations(range(5),5))
ans = math.inf
for order in stacking_order:
    ans = min(ans,go(order))
if ans == math.inf: print(-1)
else: print(ans)





