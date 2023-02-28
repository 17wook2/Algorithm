n = int(input())
arr = []
ans = 0
for i in range(n):
    arr.append(list(input()))

def check():
    global ans
    for i in range(n):
        w_cnt = 1; r_cnt = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                w_cnt += 1
            else:
                ans = max(ans,w_cnt)
                w_cnt = 1
            if arr[j][i] == arr[j+1][i]:
                r_cnt += 1
            else:
                ans = max(ans,r_cnt)
                r_cnt = 1
        ans = max(ans,w_cnt,r_cnt)

for i in range(n):
    for j in range(n-1):
        if arr[i][j] != arr[i][j+1]:
            temp = arr[i][j]
            arr[i][j] = arr[i][j+1]
            arr[i][j+1] = temp
            check()
            temp = arr[i][j]
            arr[i][j] = arr[i][j + 1]
            arr[i][j + 1] = temp
        if arr[j][i] != arr[j+1][i]:
            temp = arr[j][i]
            arr[j][i] = arr[j+1][i]
            arr[j+1][i] = temp
            check()
            temp = arr[j][i]
            arr[j][i] = arr[j + 1][i]
            arr[j + 1][i] = temp

print(ans)