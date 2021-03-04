from collections import deque
r,c = map(int,input().split())
maps = [list(input()) for i in range(r)]
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'S':
            start = (i,j)
            maps[i][j] = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def waterflow(start):
    w = deque([])
    d = deque([start])
    for i in range(r):
        for j in range(c):
            if maps[i][j] == '*':
                w.append((i,j))
    while w or d:
        w_temp = []
        d_temp = []
        while d:
            a,b = d.popleft()
            if maps[a][b] == '*':
                continue
            for k in range(4):
                na = a + dx[k]
                nb = b + dy[k]
                if 0 <= na < r and 0 <= nb < c:
                    if maps[na][nb] == 'D':
                        return maps[a][b] + 1
                    elif maps[na][nb] == '.':
                        maps[na][nb] = maps[a][b] + 1
                        d_temp.append((na,nb))
        while w:
            x,y = w.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != 'D' and maps[nx][ny] != '*' and maps[nx][ny] != 'X':
                    maps[nx][ny] = '*'
                    w_temp.append((nx,ny))

        for _ in w_temp:
            w.append(_)
        for __ in d_temp:
            d.append(__)

    return 'KAKTUS'

print(waterflow(start))

