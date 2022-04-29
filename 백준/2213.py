n = int(input())
arr = list(map(int,input().split()))
tree = [[] for i in range(n+1)]
dp = [[0]*2 for i in range(n+1)]
track = [[[],[]] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
def dfs(node,visited):
    dp[node][1] = arr[node-1]
    track[node][1].append(node)
    for x in tree[node]:
        if not visited[x]:
            visited[x] = 1
            if not dp[x][0]:
                dfs(x,visited)
            visited[x] = 0
            dp[node][1] += dp[x][0]
            track[node][1].extend(track[x][0])
            if dp[x][0] > dp[x][1]:
                dp[node][0] += dp[x][0]
                track[node][0].extend(track[x][0])
            else:
                dp[node][0] += dp[x][1]
                track[node][0].extend(track[x][1])

v = [0]*(n+1)
v[1] = 1
dfs(1,v)
if dp[1][0] > dp[1][1]:
    track[1][0].sort()
    print(dp[1][0])
    print(*track[1][0])
else:
    track[1][1].sort()
    print(dp[1][1])
    print(*track[1][1])


