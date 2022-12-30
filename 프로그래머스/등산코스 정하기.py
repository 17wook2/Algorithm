import heapq
import math
def solution(n, paths, gates, summits):
    answer = []
    ans = math.inf
    graph = [[] for i in range(n + 1)]
    for path in paths:
        a, b, w = path
        graph[a].append((b, w))
        graph[b].append((a, w))
    def go():
        q = []
        visited = [math.inf] * (n + 1)
        for gate in gates:
            heapq.heappush(q, (0, gate))
            visited[gate] = 0

        while q:
            cur_cost, cur_node = heapq.heappop(q)
            if cur_node in summits or cur_cost > visited[cur_node]: continue
            for next_node, next_cost in graph[cur_node]:
                new_cost = max(cur_cost, next_cost)
                if new_cost < visited[next_node]:
                    visited[next_node] = new_cost
                    heapq.heappush(q, (new_cost, next_node))

        for summit in summits:
            if visited[summit] < ans:
                ans = visited[summit]
                del answer[:]
                answer.append(summit)
            elif visited[summit] == ans:
                answer.append(summit)
    go()
    answer.sort()
    return [answer[0], ans]







