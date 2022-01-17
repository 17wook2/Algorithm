import copy
from collections import deque
n,m = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
cctvs = []
answer = 100
direction =  [[],
             [[0],[1],[2],[3]],
             [[0,2],[1,3]],
             [[0,1],[1,2],[2,3],[3,0]],
             [[0,1,3],[0,1,2],[1,2,3],[0,2,3]],
             [[0,1,2,3]]]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            cctvs.append((i,j))

def checkBlindSpot(room):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if room[i][j] == 0:
                cnt += 1;
    return cnt

def fill(board,x,y,d):
    for e in d:
        nx = x
        ny = y
        while True:
            nx += dx[e]
            ny += dy[e]
            if 0<=nx<n and 0<= ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = '#'
                if board[nx][ny] == 6:
                    break;
            else:
                break;

def solve(room,cnt):
    board = copy.deepcopy(room)
    global answer
    if cnt == len(cctvs):
        answer = min(answer, checkBlindSpot(room))
        return
    x,y = cctvs[cnt]
    cctvnumber = arr[x][y]
    for d in direction[cctvnumber]:
        fill(board,x,y,d)
        solve(board,cnt+1)
        board = copy.deepcopy(room)
solve(arr,0)
print(answer)









