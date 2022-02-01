answer = [-1] * 12


def compare(a, b):
    return a[::-1] > b[::-1]


def solution(n, info):
    dfs(n, 0, [0] * 12, info)
    answer.pop()
    return answer


def dfs(arrow_left, idx, lion, apeche):
    global answer
    if arrow_left < 0:
        return
    if idx >= 10:  ## dfs의 끝
        lscore = 0
        ascore = 0
        lion[10] = arrow_left
        print(arrow_left,lion)
        for j in range(10):
            if apeche[j] == 0 and lion[j] == 0:
                continue
            if lion[j] > apeche[j]:
                lscore += (10 - j)
            else:
                ascore += (10 - j)
        if lscore > ascore:
            lion[11] = lscore - ascore
            if compare(lion, answer):
                answer = lion[:]
        return
    lion[idx] = apeche[idx] + 1
    dfs(arrow_left - (apeche[idx] + 1), idx + 1, lion, apeche)
    lion[idx] = 0
    dfs(arrow_left,idx+1,lion,apeche)

print(solution(10,[0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))