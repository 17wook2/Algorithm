n = int(input())
visited = [0]*(n+1)
def dfs(d,x):
    if d == n:
        print(*x)
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = 1
            x.append(i)
            dfs(d+1,x)
            visited[i] = 0
            x.pop()
dfs(0,[])
