import heapq
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs():
    heap = []
    visited = [[0]*n for i in range(n)]
    heapq.heappush(heap,(0,0,0))
    visited[0][0] = 1
    while heap:
        cnt,x,y = heapq.heappop(heap)
        if x == n-1 and y == n-1: return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if visited[nx][ny]: continue
            visited[nx][ny] = 1
            if arr[nx][ny] == 1:
                heapq.heappush(heap,(cnt,nx,ny))
            else:
                heapq.heappush(heap,(cnt+1,nx,ny))

print(bfs())
