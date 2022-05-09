n = int(input())
x = list(input())
arr = [['.']*n for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(i,n):
        arr[i][j] = x[cnt]
        cnt += 1
ans = []
def check(idx):
    psum = 0
    for i in range(idx,-1,-1):
        psum += ans[i]
        if arr[i][idx] == '+' and psum <= 0: return False
        if arr[i][idx] == '-' and psum >= 0: return False
        if arr[i][idx] == '0' and psum != 0: return False
    return True
def dfs(idx):
    if idx == n:
        print(*ans)
        exit(0)
    for i in range(-10,11,1):
        ans.append(i)
        if check(idx):
            dfs(idx+1)
        ans.pop()

dfs(0)