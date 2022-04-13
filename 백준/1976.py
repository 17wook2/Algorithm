n = int(input())
m = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
route = list(map(int,input().split()))
route = list(map(lambda x:x-1 , route))
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] + arr[k][j] == 2:
                arr[i][j] = 1
start = route[0]
ans = "YES"
for i in range(1,len(route)):
    if start == route[i]:
        continue
    if arr[start][route[i]]:
        start = route[i]
    else:
        ans = "NO"
        break
print(ans)