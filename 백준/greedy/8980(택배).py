n,c = map(int,input().split())
m = int(input())
orders = []
for i in range(m):
    orders.append(list(map(int,input().split())))

# 시작점에서 가장 가까운 순서대로 나열
orders.sort(key = lambda x: (x[1], x[0]))
# print(orders)

# 시작점에서 목표점까지 들고갈때 가방 여유공간
# 오래들고가면 안좋음, 어짜피 분할 가능하고 빠르게 회전되야 많이 옮기기 때문에
capacity = [c]*(n+1)
answer= 0
for order in orders:
    start, end, box = order[0], order[1], order[2]
    fit_size = min(capacity[start:end])
    # 해당 구간에서의 최솟값이 현재 사이즈보다 작으면 cannot fit in
    if fit_size  == 0:
        continue
    elif fit_size >= box:
        answer += box
        for i in range(start,end):
            capacity[i] -= box
    else:
        answer += fit_size
        for i in range(start,end):
            capacity[i] -= fit_size
print(answer)



