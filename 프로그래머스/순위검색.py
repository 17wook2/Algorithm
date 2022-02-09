import bisect
combi = []
def makecombi(cnt, word, array):
    if cnt == 4:
        combi.append(word)
        return
    makecombi(cnt + 1, word + array[cnt], array)
    makecombi(cnt + 1, word + '-', array)


def solution(info, query):
    answer = []
    info_dict = {}
    for i in info:
        a, b, c, d, e = i.split(" ")
        makecombi(0, '', [a, b, c, d])
        for com in combi:
            if com in info_dict:
                info_dict[com].append(int(e))
            else:
                info_dict[com] = [int(e)]
        del combi[:]
    for k in info_dict:
        info_dict[k].sort()
    for q in query:
        tmp = ''
        a, b, c, d = q.split(" and ")
        d, e = d.split(" ")
        tmp += a
        tmp += b
        tmp += c
        tmp += d
        e = int(e)
        if tmp not in info_dict:
            answer.append(0)
            continue
        pos = bisect.bisect_left(info_dict[tmp], e)
        answer.append((len(info_dict[tmp]) - pos))
    return answer