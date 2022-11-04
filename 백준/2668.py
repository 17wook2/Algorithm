def solve(idx,target,visited):
    if graph[idx] == target:
        return True
    if not visited[graph[idx]]:
        visited[graph[idx]] = 1
        return solve(graph[idx],target,visited)
    else:
        return False


n = int(input())
ans = []
graph = [0]*(n+1)
for i in range(n):
    x = int(input())
    graph[i+1] = x
for i in range(1,n+1):
    visited = [0] * (n + 1)
    visited[i] = 1
    if solve(i,i,visited):
       ans.append(i)

print(len(ans))
for x in ans:
    print(x)






