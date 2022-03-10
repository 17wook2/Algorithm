n,m = map(int,input().split())
people = [0]*(n+1)
truth = list(map(int,input().split()))
truth = truth[1:]
for i in range(len(truth)):
    people[truth[i]] = 1
graph = [[] for i in range(n+1)]
party = []
for i in range(m):
    tmp = list(map(int,input().split()))
    tmp = tmp[1:]
    party.append(tmp)
    if len(tmp) == 1:
        continue
    for i in range(len(tmp)):
        for j in range(i+1,len(tmp)):
            graph[tmp[i]].append(tmp[j])
            graph[tmp[j]].append(tmp[i])

for start in truth:
    visited = [0]*(n+1)
    stack = [start]
    while stack:
        x = stack.pop()
        visited[x] = 1
        for j in graph[x]:
            if not visited[j]:
                people[j] = 1
                stack.append(j)
ans = 0
for p in party:
    for x in p:
        if people[x] == 1:
            break
    else:
        ans += 1
print(ans)



