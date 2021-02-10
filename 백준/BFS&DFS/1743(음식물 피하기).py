from collections import deque
import sys
n,m,k = list(map(int,sys.stdin.readline().split()))
array = [[0]*m for i in range(n)]
for i in range(k):
    r,c = list(map(int,sys.stdin.readline().split()))
    array[r-1][c-1] = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
deq = deque([])
size = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            deq.append((i,j))
            answer = 0
            while deq:
                x,y = deq.popleft()
                array[x][y] = 0
                answer += 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >=m:
                        continue
                    if array[nx][ny] == 1:
                        array[nx][ny] = 0
                        deq.append((nx,ny))
            # print(answer)
            size = max(size,answer)
print(size)
