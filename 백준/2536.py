from collections import deque
import math
m,n = map(int,input().split())
k = int(input())
arr = [0] * (k+1)
graph = [[] for i in range(k)]
is_included = [0]*(k+1)
for i in range(k):
    a,b,c,d,e = list(map(int,input().split()))
    arr[a-1] = (min(b,d),min(c,e),max(b,d),max(c,e))

for i in range(k):
    for j in range(k):
        if i == j: continue
        x1,y1,x2,y2 = arr[i]
        x3,y3,x4,y4 = arr[j]
        if x1 == x2 == x3 == x4:
            if y3 <= y1 <= y2 <= y4:
                is_included[i] = 1
        if y1 == y2 == y3 == y4:
            if x3 <= x1 <= x2 <= x4:
                is_included[i] = 1
for i in range(k):
    if is_included[i]:
        continue
    for j in range(k):
        if i == j: continue
        if is_included[j]: continue
        x1, y1, x2, y2 = arr[i]
        x3, y3, x4, y4 = arr[j]
        if x1 <= x3 <= x2 and y3 <= y1 <= y4 and y3 <= y2 <= y4:
            graph[i].append(j)
            graph[j].append(i)
        if y1 == y2 == y3 == y4:
            if not (x1 > x4 or x2 < x3):
                graph[i].append(j)
                graph[j].append(i)
        if x1 == x2 == x3 == x4:
            if not (y1 > y4 or y2 < y3):
                graph[i].append(j)
                graph[j].append(i)

start = []
end = []
sx,sy,ex,ey = list(map(int,input().split()))
for i in range(k):
    if is_included[i]:
        continue
    x1,y1,x2,y2 = arr[i]
    if x1 <= sx <= x2 and y1 <= sy <= y2:
        start.append(i)
    if x1 <= ex <= x2 and y1 <= ey <= y2:
        end.append(i)
q = deque([])

visited = [-1]*k
for node in start:
    visited[node] = 0
    q.append(node)
while q:
    x = q.popleft()
    for node in graph[x]:
        if visited[node] == -1:
            visited[node] = visited[x] + 1
            q.append(node)

ans = math.inf
for node in end:
    ans = min(ans,visited[node])

print(ans+1)