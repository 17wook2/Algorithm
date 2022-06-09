n,m = map(int,input().split())
arr = []
for i in range(n):
    x = list(input())
    arr.append(x)
check = [[0]*m for i in range(n)]
ans = 0
def func():
    ## check값이 1이면 가로 2면 세로
    visited = [[0]*m for i in range(n)]
    psum = 0
    for i in range(n):
        for j in range(m):
            tmp = ''
            if check[i][j] == 1 and not visited[i][j]:
                for k in range(j,m):
                    if check[i][k] == 1:
                        tmp += arr[i][k]
                        visited[i][k] = 1
                    else:
                        break
                psum += int(float(tmp))
    visited2 = [[0]*m for i in range(n)]
    for i in range(m):
        for j in range(n):
            tmp = ''
            if check[j][i] == 2 and not visited2[j][i]:
                for k in range(j,n):
                    if check[k][i] == 2:
                        tmp += arr[k][i]
                        visited2[k][i] = 1
                    else:
                        break
                psum += int(float(tmp))
    return psum
def dfs(x,y):
    global ans
    if x == n:
        ans = max(ans,func())
        return
    if y == m:
        dfs(x+1,0)
        return
    check[x][y] = 1
    dfs(x,y+1)
    check[x][y] = 2
    dfs(x,y+1)

dfs(0,0)
print(ans)