def compare(a, b):
    return a[::-1] > b[::-1]


def solution(n, info):
    ans = [-1] * 12
    for lionbit in range(1024):  ##
        lion = [0] * 12
        ascore = 0
        lscore = 0
        cnt = n
        for maskbit in range(10):
            x = lionbit & (1 << maskbit)
            if x:  ## 비트가 켜져 있다면 라이언이 이겨야 하는 경우
                lscore += 10 - maskbit
                lion[maskbit] = info[maskbit] + 1
                cnt -= lion[maskbit]
            elif info[maskbit] != 0:  ## 어피치가 이기는 경우
                ascore += 10 - maskbit
        if lscore <= ascore or cnt < 0:
            continue
        lion[10] = cnt
        lion[11] = lscore - ascore
        if compare(lion, ans):
            ans = lion[:]
    if ans[-1] == -1:
        return [-1]
    else:
        ans.pop()
        return ans

