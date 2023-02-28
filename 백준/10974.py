n = int(input())
visited = [0]*(n+1)
def go(cnt,x):
    if cnt == n+1:
        print(*x)
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = 1
            x.append(i)
            go(cnt+1,x)
            visited[i] = 0
            x.pop()
go(1,[])
