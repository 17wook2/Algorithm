n = int(input())
k = int(input())
dp = [[-1]*(n+1) for i in range(n+1)]
def dfs(cur,cnt):
    if cnt == 1:
        return cur
    if cur <= 0 or cur < 2*cnt:
        return 0
    if dp[cur][cnt] != -1:
        return dp[cur][cnt]
    dp[cur][cnt] = (dfs(cur-1,cnt) + dfs(cur-2,cnt-1)) % 1000000003
    return dp[cur][cnt]
print(dfs(n,k))
