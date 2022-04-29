import sys
sys.setrecursionlimit(10**5)
n = int(input())
arr = list(map(int,input().split()))
tree = [[] for i in range(n+1)]
dp = [[0]*2 for i in range(n+1)] ## 0이면 우수
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0]*(n+1)
def dfs(node):
    visited[node] = 1
    dp[node][0] = arr[node-1]
    for x in tree[node]:
        if not visited[x]:
            dfs(x)
            dp[node][0] += dp[x][1] ## 우수 마을이면 주변 마을 우수마을이면 안된다.
            dp[node][1] += max(dp[x][0], dp[x][1])
dfs(1)
print(max(dp[1]))