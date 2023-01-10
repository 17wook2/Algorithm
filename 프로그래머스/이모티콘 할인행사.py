def solution(users, emoticons):
    def getPrice():
        prices = []
        for e in emoticons:
            p = []
            for d in discount:
                price = e * (100 - d) * 0.01
                p.append(int(price))
            prices.append(p)
        return prices

    def go():
        res = [0, 0]
        for user in users:
            purchased = 0
            percent, bound = user
            for i in range(e_cnt):
                for j in range(4):
                    if check[i][j]:
                        if percent <= discount[j]:  ## 할인을 더 많이 하면
                            purchased += prices[i][j]
            if purchased >= bound:  ## 가격 이상의 이모티콘 구매
                res[0] += 1
            else:
                res[1] += purchased
        answer.append(res)

    def dfs(idx):
        if idx == e_cnt:
            go()
            return
        for i in range(4):
            check[idx][i] = 1
            dfs(idx + 1)
            check[idx][i] = 0

    answer = []
    discount = [10, 20, 30, 40]
    prices = getPrice()
    e_cnt = len(emoticons)
    check = [[0] * 4 for i in range(e_cnt)]
    dfs(0)
    answer.sort(key=lambda x: (x[0], x[1]), reverse=True)

    return answer[0]