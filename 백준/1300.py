#unsolved
a = int(input())
b = int(input())
start = 1
end = b
while start <= end:
    # print(start,end)
    mid = (start + end) // 2 # mid 값보다 큰거 있는지 확인
    cnt = 0
    for i in range(1,a+1):
        cnt += min(mid//i,a)
    if cnt < b:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1
print(answer)