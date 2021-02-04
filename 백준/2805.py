n,m = list(map(int,input().split()))
trees = list(map(int,input().split()))
start = 1
end = max(trees)
while start <= end:
    mid = (start+end) // 2
    take = 0
    for tree in trees:
        if tree - mid > 0:
            take += tree - mid
    if take >= m: # 더 높이 잘라야 할때
        start = mid + 1
    elif take < m: # 더 낮게 잘라야 할때
        end = mid - 1
print(end)
