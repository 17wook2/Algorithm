a = int(input())
b = int(input())
start = 1
end = b
while start < end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1,a+1):
        cnt += min(mid//i, a)
    if cnt >= b:
        end = mid
    else:
        start = mid + 1

print(end)