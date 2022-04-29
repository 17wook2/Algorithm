import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n+1)]
dp = [[0,0] for i in range(n+1)] ## 0이면 얼리어답터
visited = [0]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
def dfs(node):
    dp[node][0] = 1
    visited[node] = 1
    for x in tree[node]:
        if not visited[x]:
            dfs(x)
            dp[node][1] += dp[x][0]
            dp[node][0] += min(dp[x][0], dp[x][1])
dfs(1)
print(min(dp[1]))
