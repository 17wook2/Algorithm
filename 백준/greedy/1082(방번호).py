n = int(input())
idx = [i for i in range(n)]
cost = list(map(int,input().split()))
market = list(zip(idx,cost))
wallet = int(input())
# print(cost)
# print(market)
try:
    a = sorted(market[1:len(market)], key = lambda x:x[1])[0]
except IndexError:
    a = market[0]
b = sorted(market, key = lambda x:x[1])[0]
answer = ''
acc = 0
acc += a[1]
answer += str(a[0])
while acc + b[1] <= wallet:
    acc += b[1]
    answer += str(b[0])
# print(answer)
# print(acc)
# 문자열 하나씩 순회해 가면서
# market.sort(key = lambda x:x[1])
# print(market)
revised = ''
for k in answer:
    t = n-1 # 제일 큰값
    while True:
        if acc - cost[int(k)] + cost[t] <= wallet: # 전체비용 - 현재자리수 비용 + 제일 큰수 자리수 비용
            acc -= cost[int(k)]
            acc += cost[t]
            break
        else:
            t -= 1
    revised += str(market[t][0])
print(revised)