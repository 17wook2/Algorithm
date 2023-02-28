t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int,input().split()))
    idx = n-1
    max_price = 0
    profit = 0
    while idx >= 0:
        if prices[idx] > max_price:
            max_price = prices[idx]
        else:
            profit += (max_price - prices[idx])
        idx -= 1
    print(profit)
