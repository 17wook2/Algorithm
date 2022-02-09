import math
from collections import defaultdict
from collections import deque


def solution(n, s, a, b, fares):
    graph = [[math.inf] * (n + 1) for i in range(n + 1)]
    connect = defaultdict(list)
    for fare in fares:
        connect[fare[0]].append(fare[1])
        connect[fare[1]].append(fare[0])
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]

    for k in range(n + 1):
        graph[k][k] = 0
        for i in range(n + 1):
            for j in range(n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    answer = graph[s][a] + graph[s][b]
    visited = [0] * (n + 1)
    queue = deque([])
    queue.append(s)
    while queue:
        x = queue.popleft()
        for node in connect[x]:
            if visited[node]:
                continue
            else:
                visited[node] = 1
                tmp = graph[s][node] + graph[node][a] + graph[node][b]
                if tmp <= answer:
                    answer = tmp
                    queue.append(node)

    return answer