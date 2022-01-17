import math
n,s = list(map(int,input().split()))
arr = list(map(int,input().split()))
i=0
j=1
tmp = arr[i] + arr[j]
ans = math.inf
while j < len(arr) and i < len(arr):
    if i > j:
        tmp += arr[i]
        tmp -= arr[j]
        j += 1
    if tmp < s:
        j += 1
        if j < len(arr):
            tmp += arr[j]
    elif tmp >= s:
        ans = min(ans,j-i+1)
        tmp -= arr[i]
        i += 1

if ans == math.inf:
    print(0)
else:
    print(ans)