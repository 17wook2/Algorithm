from collections import deque
n = int(input())
array = [list(map(int,input().split())) for i in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def arraytobinary(water):
    x = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if array[i][j] > water:
                x[i][j] = 1
            else:
                x[i][j] = 0
    return x
def bfs(region):
    count = 0
    # print(region)
    for i in range(n):
        for j in range(n):
            if region[i][j] == 0: # 0이면 침수지역
                continue
            else:
                count += 1
                queue = deque([(i,j)])
                while queue:
                    x,y = queue.popleft()
                    region[x][y] = 0
                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]
                        if 0 <= nx < n and 0 <= ny < n and region[nx][ny] == 1:
                            region[nx][ny] = 0
                            queue.append((nx,ny))
    return count
def findmax():
    temp = 0
    for i in range(n):
        for j in range(n):
            temp = max(temp,array[i][j])
    return temp
# 감소하는 지점 찾기
k = findmax()
answer = 0
for i in range(k+1):
    new_array = arraytobinary(i)
    answer = max(answer,bfs(new_array))
print(answer)