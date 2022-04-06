import sys
input = sys.stdin.readline
v = int(input())
graph = [[] for i in range(v+1)]
for i in range(v):
    arr = list(map(int,input().split()))
    for j in range(1,len(arr)-1,2):
        graph[arr[0]].append((arr[j],arr[j+1]))
def dfs(start,visited):
    for node in graph[start]:
        if not visited[node[0]]:
            visited[node[0]] = visited[start] + node[1]
            dfs(node[0],visited)
arr = [0]*(v+1)
dfs(1,arr)
arr2 = [0]*(v+1)
idx = arr.index(max(arr))
arr2[idx] = 1
dfs(idx,arr2)
print(max(arr2)-1)