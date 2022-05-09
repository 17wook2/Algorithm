n = int(input())
arr = list(map(int,input().split()))
idx = 0
for i in range(n-1,0,-1):
    if arr[i-1] < arr[i]:
        idx = i-1
        break
for i in range(n-1,0,-1):
    if arr[idx] < arr[i]:
        arr[idx],arr[i] = arr[i],arr[idx]
        arr = arr[:idx+1] + sorted(arr[idx+1:])
        print(*arr)
        exit()
print(-1)

