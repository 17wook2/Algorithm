import heapq
import math
n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
distance = [math.inf]*(n+1)
for i in range(m):
    a,b,c = list(map(int,input().split()))
    graph[a].append((b,c))
start,end = list(map(int,input().split()))
arr = [[i] for i in range(n+1)]
distance[start] = 0
def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,start))
    while heap:
        dist,now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]: ## node를 거쳐가는 경우 비용이 더 싼 경우
                arr[node[0]] = arr[now][:]
                arr[node[0]].append(node[0])
                distance[node[0]] = cost
                heapq.heappush(heap,(cost,node[0]))
dijkstra(start)
print(distance[end])
print(len(arr[end]))
print(*arr[end])
