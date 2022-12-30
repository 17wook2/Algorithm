import math
import sys
input = sys.stdin.readline
def check(x,y):
    if 0 <= x < 5 and 0 <= y < 9:
        return True
    return False
def dfs(move):
    global min_move, min_cnt
    for x in range(5):
        for y in range(9):
            if arr[x][y] == 'o':
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    nnx = nx + dx[k]
                    nny = ny + dy[k]
                    if check(nx,ny) and check(nnx,nny) and arr[nx][ny] == 'o' and arr[nnx][nny] == '.':
                        arr[x][y] = '.'
                        arr[nx][ny] = '.'
                        arr[nnx][nny] = 'o'
                        dfs(move+1)
                        arr[x][y] = 'o'
                        arr[nx][ny] = 'o'
                        arr[nnx][nny] = '.'
    cnt = 0
    for i in range(5):
        for j in range(9):
            if arr[i][j] == 'o':
                cnt += 1
    if cnt < min_cnt:
        min_cnt = cnt
        min_move = move
    elif cnt == min_cnt:
        min_move = min(min_move, move)
    return
t = int(input())
for i in range(t):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    arr = []
    min_move = math.inf
    min_cnt = math.inf
    for i in range(5):
        arr.append(list(input()))
    dfs(0)
    print(min_cnt,min_move)
    input()