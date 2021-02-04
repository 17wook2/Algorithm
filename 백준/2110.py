n,c = list(map(int,input().split()))
lst =[]
for i in range(n):
    lst.append(int(input()))
lst.sort()
max_length = lst[-1] - lst[0]
start = 0
end = max_length
while start <= end:
    unit = (start + end)
    mid = unit // 2
    temp = lst[0]
    count = 1
    for i in range(1,n):
        if temp + mid <= lst[i]:
            count += 1
            temp = lst[i]
    # print(count)
    if count >= c:
        start = mid + 1
    else:
        end = mid - 1
print(end)