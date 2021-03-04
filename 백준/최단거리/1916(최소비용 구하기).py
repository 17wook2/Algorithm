import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize
V = int(input())
e = int(input())
graph = [[] for i in range(V+1)]
distance = [inf]*(V+1)
for i in range(e):
    u,v,w = map(int,input().split()) # 시작 끝 거리
    graph[u].append((v,w))
start,end = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 시작점은 0
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist: # 방문한 적이 있다면
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
        # print(distance)

dijkstra(start)

print(distance[end])