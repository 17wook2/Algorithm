import heapq
import math
n,d = list(map(int,input().split()))
distance = [math.inf]*(d+1)
graph = [[] for i in range(d+1)]
for i in range(d):
    graph[i].append((i+1,1))
for i in range(n):
    start,end,time = list(map(int,input().split()))
    if end > d: continue
    graph[start].append((end,time))

def dijkstra():
    heap = []
    heapq.heappush(heap,(0,0))
    distance[0] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if dist > distance[now]: continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(heap,(cost,node[0]))
dijkstra()
print(distance[d])
