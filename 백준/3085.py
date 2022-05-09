n = int(input())
arr = []
ans = 0
for i in range(n):
    arr.append(list(input()))
def check():
    global ans
    for i in range(n):
        w_cnt = 1
        h_cnt = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                w_cnt += 1
            else:
                ans = max(ans,w_cnt)
                w_cnt = 1
            if arr[j][i] == arr[j+1][i]:
                h_cnt += 1
            else:
                ans = max(ans,h_cnt)
                h_cnt = 1
        ans = max(ans,w_cnt,h_cnt)

check()
for i in range(n):
    for j in range(n-1):
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            check()
            arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
        if arr[j][i] != arr[j+1][i]:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            check()
            arr[j+1][i],arr[j][i] = arr[j][i], arr[j+1][i]

print(ans)
