n,target = list(map(int,input().split()))
arr = list(map(int,input().split()))
ans = 100001
prefix_sum,s,e = 0,0,0
while True:
    if prefix_sum >= target:
        prefix_sum -= arr[s]
        ans = min(ans, e-s)
        s += 1
    elif e == n:
        break
    else:
        prefix_sum += arr[e]
        e += 1

if ans == 100001:
    print(0)
else:
    print(ans)
