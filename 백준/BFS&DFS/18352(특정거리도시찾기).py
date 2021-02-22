from collections import deque
n,m,k,x = list(map(int,input().split()))
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
# print(graph)
queue = deque([x])
visited = [0]*(n+1)
distance = [0]*(n+1)
while queue:
    temp = queue.popleft()
    visited[temp] = 1
    for v in graph[temp]:
        if not visited[v]:
            queue.append(v)
            visited[v] = 1
            distance[v] = distance[temp] + 1
# print(distance)
if k not in distance:
    print(-1)
else:
    for i in range(1,len(distance)):
        if distance[i] == k:
            print(i)