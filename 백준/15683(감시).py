import copy
from collections import deque
n,m = list(map(int,input().split()))
room = []
for i in range(n):
    room.append(list(map(int,input().split())))
cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= room[i][j] <= 5:
            cctv.append([room[i][j],i,j])

answer = 100
dx = [1,-1,0,0] ## bottom top right left
dy = [0,0,1,-1]

direction = [[],[[0],[1],[2],[3]] , [[0,1],[2,3]], [[3,0],[0,2],[2,1],[1,3]], [[1,3,0],[3,0,2],[0,2,1],[2,1,3]], [[0,1,2,3]] ]

def fill(x, y, board, e):
    for ele in e:
        nx = x
        ny = y
        while True:
            nx += dx[ele]
            ny += dy[ele]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 6:
                    break
                elif board[nx][ny] == 0:
                    board[nx][ny] = '#'
            else:
                break

def solve(graph, cnt):
    global answer
    board = copy.deepcopy(graph)
    if cnt == len(cctv):  ## cctv다 썻다면
        a = 0
        for row in graph:
            a += row.count(0)
        answer = min(answer, a)
        return
    else:
        t, x, y = cctv[cnt]
        for e in direction[t]:
            fill(x, y, board, e)
            solve(board, cnt + 1)
            board = copy.deepcopy(graph)
solve(room,0)
print(answer)


