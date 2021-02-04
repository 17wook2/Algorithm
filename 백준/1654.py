n,k = list(map(int,input().split()))
lst = [int(input()) for i in range(n)]
# lst의 가장 긴 선 기준으로
start = 1
end = max(lst)
while start <= end:
    mid = (end + start) // 2
    # print(start, end)
    cut = 0
    for lan in lst:
        cut += lan // mid
    if cut >= k:
        start = mid + 1
    else:  # k보다 못자르면
        end = mid - 1
print(end)

