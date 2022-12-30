n = int(input())
arr = list(map(int,input().split()))
cnt = 0; e = 0
visited = [0]*100001
for s in range(n):
    while e < n:
        if visited[arr[e]]:
            break
        visited[arr[e]] = 1
        e += 1
    cnt += e - s
    visited[arr[s]] = 0
print(cnt)