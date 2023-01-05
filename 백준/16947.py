import sys
sys.setrecursionlimit(10**7)
from collections import deque
n = int(input())
graph = [[] for i in range(n)]
for i in range(n):
    a,b = map(int,input().split())
    a -= 1; b-=1;
    graph[a].append(b)
    graph[b].append(a)
hasCycle = False
cycles = [0]*n
parent = [i for i in range(n)]
visited = [0]*n
dist = [0]*n
def solve(cur):
    global hasCycle
    visited[cur] = 1
    for node in graph[cur]:
        if hasCycle: return
        if visited[node]:
            if node != parent[cur]:
                hasCycle = True
                cycles[cur] = 1
                while cur != node:
                    cycles[parent[cur]] = 1
                    cur = parent[cur]
                return
        else:
            parent[node] = cur
            solve(node)
def bfs():
    q = deque()
    for i in range(n):
        if cycles[i]:
            visited[i] = 1
            q.append((i,0))
    while q:
        x,d = q.popleft()
        visited[x] = 1
        for next in graph[x]:
            if visited[next]: continue
            dist[next] = d + 1
            q.append((next,d+1))

solve(0)
visited = [0]*n
bfs()
print(*dist)