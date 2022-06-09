n = int(input())
arr = list(map(int,input().split()))
idx = 0
ans = []
for i in range(n-1):
    if arr[i] > arr[i+1]:
        idx = i
for i in range(n-1,0,-1):
    if arr[idx] > arr[i]:
        arr[idx],arr[i] = arr[i], arr[idx]
        ans = arr[0:idx+1] + sorted(arr[idx+1:],reverse=True)
        print(*ans)
        exit()
print(-1)
