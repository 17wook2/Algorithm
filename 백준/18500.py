from collections import deque
def adjust():
    visited = [[0]*c for i in range(r)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    cluster = 0
    queue = deque([])
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and array[i][j] == 'x':
                cluster += 1
                visited[i][j] = cluster
                queue.append((i,j))
                while queue:
                    x,y = queue.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < r and 0 <= ny < c and array[nx][ny] == 'x' and not visited[nx][ny]:
                            visited[nx][ny] = cluster
                            queue.append((nx,ny))
    dist_dict = {}
    for idx in range(1, cluster + 1):
        dist = get_distance(idx,visited)
        dist_dict[idx] = dist
    for i in range(r-1,-1,-1):
        for j in range(c-1,-1,-1):
            if array[i][j] != '.':
                dist = dist_dict[visited[i][j]]
                array[i][j] = '.'
                array[i+dist][j] = 'x'

def get_distance(cluster,visited):
    d = r
    for i in range(r-1,-1,-1):
        for j in range(c-1,-1,-1):
            t = 0
            if visited[i+t][j] == cluster:
                while i+t < r-1 and (visited[i+t+1][j] == cluster or visited[i+t+1][j] == 0):
                    t += 1

                d = min(d,t)
    return d


def shoot(direction,height):
    if direction == 'L':
        for i in range(c):
            if array[height][i] == 'x':
                array[height][i] = '.'
                break
    elif direction == 'R':
        for i in range(c-1,-1,-1):
            if array[height][i] == 'x':
                array[height][i] = '.'
                break

def simulate():
    for i in range(len(h)):
        if i % 2 == 0:
            shoot('L',h[i])
        else:
            shoot('R',h[i])
        adjust()
    return

r,c = map(int,input().split())
array = []
for i in range(r):
    array.append(list(input()))
n = int(input())
h = list(map(int,input().split()))
for i in range(n):
    h[i] = r - h[i]

simulate()

for i in range(r):
    for j in range(c):
        print(array[i][j],end='')
    print()