def solution(today, terms, privacies):
    answer = []
    tday = getdays(today)
    terms_dict = {}
    for term in terms:
        term = term.split(" ")
        terms_dict[term[0]] = int(term[1])
    for i,privacy in enumerate(privacies):
        d, t = privacy.split(" ")
        days = getdays(d)
        days += (terms_dict[t] * 28)
        if days <= tday:
            answer.append(i+1)
    return answer

def getdays(d):
    days = 0
    date = d.split(".")
    days += (int(date[0]) - 2000)*12*28
    days += (int(date[1]) - 1) * 28
    days += int(date[2])
    return days