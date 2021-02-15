from collections import deque
from functools import reduce
m,n,h = list(map(int,input().split()))
box = [[[] for i in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        row = list(map(int,input().split()))
        for a in row:
            box[i][j].append(a)
queue = deque([])
visited = [[[0]*m for i in range(n)] for _ in range(h)]
da = [0,0,0,0,-1,1]
db = [0,0,-1,1,0,0]
dc = [-1,1,0,0,0,0]
answer = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i,j,k))
while queue:
    a,b,c = queue.popleft() # 높이 세로 가로
    for i in range(6):
        na = a + da[i]
        nb = b + db[i]
        nc = c + dc[i]
        if 0<= na < h and 0<= nb < n and 0 <= nc < m:
            if box[na][nb][nc] == 0:
                box[na][nb][nc] = box[a][b][c] + 1
                queue.append((na,nb,nc))
def check():
    answer = 0
    for height in box:
        for row in height:
            for column in row:
                if column == 0:
                    return -1
                if column == -1:
                    continue
                answer = max(answer, column)
    return answer
answer = check()
print(answer if answer == -1 else answer-1)






