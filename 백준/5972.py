import heapq
import math
n,m = list(map(int,input().split()))
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = list(map(int,input().split()))
    graph[a].append((c,b))
    graph[b].append((c,a))
distance = [math.inf]*(n+1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        value, now = heapq.heappop(q)
        for x in graph[now]:
            dist, node = x
            if distance[node] > value + dist:
                distance[node] = value + dist
                heapq.heappush(q, (distance[node], node))

dijkstra(1)
print(distance[n])