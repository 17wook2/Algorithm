from collections import deque
import math
n,q = list(map(int,input().split()))
edges = []
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,r = list(map(int,input().split()))
    graph[a].append((b,r))
    graph[b].append((a,r))

def bfs(start,k):
    queue = deque([])
    queue.append((start,math.inf))
    visited = [0]*(n+1)
    cnt = 0
    while queue:
        x,xl = queue.popleft()
        visited[x] = 1
        if xl < k:
            continue
        for v,vl in graph[x]:
            if not visited[v]:
                visited[v] = 1
                if vl >= xl: ## 아래로 더 갈수 있는경우
                    queue.append((v,xl))
                    cnt += 1
                else: ## 최솟값 갱신인 경우
                    if vl >= k:
                        queue.append((v,vl))
                        cnt += 1
    return cnt

for i in range(q):
    k,v = list(map(int,input().split()))
    print(bfs(v,k))

