n,k = map(int,input().split())
coin = []
answer = 0
for i in range(n):
    coin.append(int(input()))
for c in range(len(coin)-1,-1,-1):
    if k < coin[c]:
        continue
    else:
        while k != 0 and k-coin[c] >= 0:
            k -= coin[c]
            # print(c,k)
            answer += 1
    if k == 0:
        break;
print(answer)