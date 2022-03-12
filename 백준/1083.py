n = int(input())
arr = list(map(int,input().split()))
k = int(input())
cnt = 0
for i in range(n):
    if k == 0:
        break
    x = arr[i]
    idx = i
    for j in range(i+1,i+1+k):
        if j == n:
            break
        if x < arr[j]:
            x = arr[j]; idx = j
    k -= idx-i
    for j in range(idx,i,-1):
        arr[j] = arr[j-1]
    arr[i] = x

print(*arr)
