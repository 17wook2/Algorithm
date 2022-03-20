import math
n = int(input())
w = []
for i in range(n):
    w.append(list(map(int,input().split())))

circuit = (1<<n) - 1
dp = [[math.inf]*(1<<n) for i in range(n)] ## k번째 도시에서 k번째 도시로 오는데 최솟값
## 시작 도시는0번
def dfs(node,visited):
    if visited == circuit:
        if w[node][0]:
            return w[node][0]
        else:
            return math.inf
    if dp[node][visited] != math.inf: ## dp되어있다면 반환
        return dp[node][visited]

    for i in range(1,n):
        if w[node][i] and not visited & (1<<i):
            dp[node][visited] = min(dp[node][visited], dfs(i,visited|(1<<i)) + w[node][i])
    return dp[node][visited]

print(dfs(0,1<<0))