import math
n = int(input())
arr = list(map(int,input().split()))
s = 0; e = n-1
target = math.inf
ans_s, ans_e = 0,0
while s < e:
    v = arr[s] + arr[e]
    diff = abs(v)
    if diff <= target:
        target = diff
        ans_s = s; ans_e = e;
    if v > 0:
        e -= 1
    elif v < 0:
        s += 1
    else:
        break
print(arr[ans_s], arr[ans_e])