from collections import deque
n,l,r = list(map(int,input().split()))
city = [list(map(int,input().split())) for i in range(n)]
t_count = 0

def solution(x,y,index):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    united = []
    united.append((x,y))
    q = deque()
    q.append((x,y))
    union[x][y] = index
    summary = city[x][y]
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(city[nx][ny] - city[x][y]) <= r:
                    q.append((nx,ny))
                    union[nx][ny] = index
                    summary += city[nx][ny]
                    count += 1
                    united.append((nx,ny))
    for i,j in united:
        city[i][j] = summary // count
    return count

while True:
    union = [[-1] * n for i in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                solution(i,j,index)
                index += 1
    if index == n * n:
        break
    t_count += 1
print(t_count)

