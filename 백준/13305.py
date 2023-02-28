n = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))
idx = 0
res = 0
while idx < n-1:
    cur = idx
    for i in range(cur+1,n):
        cur = i
        if cost[cur] < cost[idx]: ## 더 싼 주유소가 있다면
            break
    res += sum(dist[idx:cur])*cost[idx]
    idx = cur

print(res)
