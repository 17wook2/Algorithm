n = int(input())
guilty = list(map(int,input().split()))
r = []
for i in range(n):
    r.append(list(map(int,input().split())))
c = int(input())
ans = 0
def dfs(remain,guilt,killed,night_passed):
    global ans
    if killed[c]:
        ans = max(ans,night_passed)
        return
    if remain % 2== 0:
        for i in range(n):
            if not killed[i]:
                killed[i] = 1
                for j in range(n):
                    guilt[j] += r[i][j]
                dfs(remain-1,guilt,killed, night_passed + 1)
                killed[i] = 0
                for j in range(n):
                    guilt[j] -= r[i][j]
    else:
        g = 0; idx = 0
        for i in range(n-1,-1,-1):
            if guilt[i] >= g and not killed[i]:
                idx = i
                g = guilt[i]
        killed[idx] = 1
        dfs(remain-1,guilt,killed,night_passed)
        killed[idx] = 0

dfs(n,guilty,[0]*n,0)

print(ans)