from collections import deque
import copy
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    build_time = [0]
    build_time.extend(list(map(int,input().split())))
    graph = [[] for i in range(n+1)]
    degree = [0]*(n+1)
    complete_time = copy.deepcopy(build_time)
    for i in range(k):
        a,b = map(int,input().split())
        degree[b] += 1
        graph[a].append(b)
    w = int(input())
    queue = deque([])
    for i in range(1,n+1):
        if degree[i] == 0:
            queue.append(i)

    while queue:
        idx = queue.popleft()
        for element in graph[idx]:
            degree[element] -= 1
            complete_time[element] = max(complete_time[element], build_time[element] + complete_time[idx])
            if degree[element] == 0:
                queue.append(element)
    print(complete_time[w])


