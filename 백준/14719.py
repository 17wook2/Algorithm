h,w = list(map(int,input().split()))
lst = list(map(int,input().split()))
arr = [[] for i in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if lst[j] >= h-i:
            arr[i].append(j)

for array in arr:
    if len(array) <= 1:
        continue
    for i in range(len(array)-1):
        if array[i+1] - array[i] > 1:
            ans += array[i+1] - array[i] - 1

print(ans)
