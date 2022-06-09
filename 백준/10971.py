n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
ans = 999999999
def tsp(start,depth,visited):
    global ans
    if depth == n-1:
        if arr[start][0] != 0:
            ans = min(ans,sum(visited) + arr[start][0])
        return
    for i in range(n):
        if i != 0 and not visited[i] and arr[start][i] != 0:
            visited[i] = arr[start][i]
            tsp(i,depth+1,visited)
            visited[i] = 0

tsp(0,0,[0]*(n+1))
print(ans)