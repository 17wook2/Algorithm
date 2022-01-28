def solution(id_list, report, k):
    answer = []
    report = list(set(report))  ## 중복 제거
    ban_dictionary = {}
    getReport = {}
    for r in report:
        a, b = r.split()
        if b not in ban_dictionary:
            ban_dictionary[b] = [a]
        else:
            ban_dictionary[b].append(a)
    for blist in ban_dictionary:
        if len(ban_dictionary[blist]) >= k:  ## 정지 당했다면
            for idl in ban_dictionary[blist]:
                if idl not in getReport:
                    getReport[idl] = 1
                else:
                    getReport[idl] += 1
    for idl in id_list:
        if idl not in getReport:
            answer.append(0)
        else:
            answer.append(getReport[idl])

    return answer