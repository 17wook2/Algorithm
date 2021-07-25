from collections import deque
from itertools import combinations
n = int(input())
population = list(map(int,input().split()))
population = [0] + population
graph = [[] for i in range(n+1)]
for i in range(1,n+1):
    lst = list(map(int,input().split()))
    for j in range(1,len(lst)):
        graph[i].append(lst[j])
answer = 10000
def bfs(area):
    queue = deque([area[0]])
    visited = [0 for _ in range(n+1)]
    cnt, ans = 1,0
    visited[area[0]] = 1
    while queue:
        x = queue.popleft()
        ans += population[x]
        for e in graph[x]:
            if e in area and not visited[e]:
                visited[e] = 1
                cnt += 1
                queue.append(e)
    if cnt == len(area):
        return ans
    else:
        return 0

for i in range(1,n//2 + 1):
    area_combination = list(combinations(range(1,n+1),i))
    for area in area_combination:
        area = list(area)
        area_set = set(area)
        area2 = set([j for j in range(1,n+1)])
        area2 = area2 - area_set
        area2 = list(area2)
        sum1 = bfs(area) ## 연결이 안되어 있다면 음수
        sum2 = bfs(area2)
        if sum1 == 0 or sum2 == 0:
            continue
        answer = min(answer, abs(sum1 - sum2))

if answer == 10000:
    print(-1)
else:
    print(answer)


