import math
def solution(n, s, a, b, fares):
    graph = [[math.inf] * (n + 1) for i in range(n + 1)]
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]
    for k in range(n + 1):
        graph[k][k] = 0
        for i in range(n + 1):
            for j in range(n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    answer = math.inf
    for i in range(1,n+1):
        answer = min(answer,graph[s][i]+graph[i][a]+graph[i][b])

    return answer


import math
import heapq
def dijkstra(graph, start):
    distance = [math.inf] * (len(graph) + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        cost, src = heapq.heappop(heap)
        for c, n in graph[src]:
            c += cost
            if c < distance[n]:
                distance[n] = c
                heapq.heappush(heap, [c, n])
    return distance


def solution(n, s, a, b, fares):
    graph = [[] for i in range(n + 1)]
    for fare in fares:
        graph[fare[0]].append([fare[2], fare[1]])
        graph[fare[1]].append([fare[2], fare[0]])
    ans = math.inf
    for i in range(1, n + 1):
        distance = dijkstra(graph, i)
        ans = min(ans, distance[s] + distance[a] + distance[b])

    return ans