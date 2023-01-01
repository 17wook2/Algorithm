import math
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
ans = math.inf
visited = [0]*20
def dfs(cnt):
    global ans
    if cnt == n:
        ans = min(ans,go())
        return
    visited[cnt] = 1
    dfs(cnt+1)
    visited[cnt] = 0
    dfs(cnt+1)

def go():
    left = 0; right = 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]: left += arr[i][j]
            elif not visited[i] and not visited[j]: right += arr[i][j]
    return abs(left-right)
dfs(0)
print(ans)