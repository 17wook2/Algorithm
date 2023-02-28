t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0]
    arr.extend(list(map(int,input().split())))
    visited = [0]*(n+1)
    cnt = 0
    def go(x):
        if not visited[arr[x]]:
            visited[arr[x]] = 1
            go(arr[x])
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            go(i)
    print(cnt)