import math
n = int(input())
arr = list(map(int,input().split()))
ans = 0
for k in range(n):
    left_acc = math.inf
    right_acc = -math.inf
    cnt = 0
    for i in range(k-1,-1,-1):
        tmp_acc = (arr[k]-arr[i]) / (k-i)
        if tmp_acc < left_acc:
            left_acc = tmp_acc
            cnt += 1
    for i in range(k+1,n):
        tmp_acc = (arr[k] - arr[i]) / (k-i)
        if tmp_acc > right_acc:
            right_acc = tmp_acc
            cnt += 1
    ans = max(ans,cnt)
print(ans)
