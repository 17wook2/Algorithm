from itertools import combinations
from collections import Counter


def solution(orders, courses):
    answer = []
    tmp = []
    for order in orders:
        for course in courses:
            if len(order) < course:
                continue
            t = list(combinations(range(len(order)), course))
            for arr in t:
                comb = ''
                for idx in arr:
                    comb += order[idx]
                comb = ''.join(sorted(comb))
                tmp.append(comb)
    count = Counter(tmp).most_common()
    courselenmax = [1] * 12
    for i in range(len(count)):
        cnt = len(count[i][0])
        courselenmax[cnt] = max(courselenmax[cnt], count[i][1])
    for i in range(len(count)):
        cnt = len(count[i][0])
        if courselenmax[cnt] == count[i][1] and count[i][1] > 1:
            answer.append(count[i][0])
    answer.sort()
    return answer