def solve(idx):
    global ans
    s,e = 0,length-1
    value = arr[idx]
    while s < e:
        p_sum = arr[s] + arr[e]
        if s == idx:
            s += 1
            continue
        if e == idx:
            e -= 1
            continue
        if p_sum == value:
            ans += 1
            return
        if p_sum < value:
            s += 1
        elif p_sum > value:
            e -= 1

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
length = len(arr)
ans = 0
for i in range(n):
    solve(i)
print(ans)
