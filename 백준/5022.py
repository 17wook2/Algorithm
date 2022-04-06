from collections import deque
n,m = list(map(int,input().split()))
arr = [[0]*(m+1) for i in range(n+1)]
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
b1 = list(map(int,input().split()))
b2 = list(map(int,input().split()))
arr[a1[0]][a1[1]] = 1
arr[a2[0]][a2[1]] = 1
arr[b1[0]][b1[1]] = 2
arr[b2[0]][b2[1]] = 2
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = 9999999
def bfs(start,end,start2,end2,c):
    global ans
    queue = deque([])
    min_distance = abs(start[0]-end[0]) + abs(start[1] - end[1])
    queue.append((start[0],start[1],0,[(start[0],start[1])]))
    visited = [[0]*(m+1) for i in range(n+1)]
    while queue:
        x,y,cnt,path = queue.popleft()
        visited[x][y] = 1
        if cnt > min_distance:
            continue
        if x == end[0] and y == end[1]:
            visited2 = [[0]*(m+1) for i in range(n+1)]
            queue2 = deque([])
            queue2.append((start2[0],start2[1],0))
            while queue2:
                q2x,q2y,cnt2 = queue2.popleft()
                visited2[q2x][q2y] = 1
                print(end2,q2x,q2y)
                if q2x == end2[0] and q2y == end2[1]:
                    print(path)
                    print(cnt2,min_distance, start)
                    print('------')
                    ans = min(ans,min_distance + cnt2)
                    continue
                for _ in range(4):
                    nq2x = q2x + dx[_]
                    nq2y = q2y + dy[_]
                    if 0 <= nq2x < n and 0 <= nq2y < m and (nq2x,nq2y) not in path and not visited2[nq2x][nq2y]:
                        visited2[nq2x][nq2y] = 1
                        queue2.append((nq2x,nq2y,cnt2+1))
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] != c:
                new_path = path[:]
                new_path.append((nx,ny))
                queue.append((nx,ny,cnt+1,new_path))

bfs(a1,a2,b1,b2,2)
bfs(b1,b2,a1,a2,1)

print(ans)