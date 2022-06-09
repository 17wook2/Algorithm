from collections import defaultdict
def solution(survey, choices):
    ans = ''
    res = defaultdict(int)
    for i in range(len(survey)):
        ques = survey[i]
        left = ques[0]; right = ques[1]; choice = choices[i];
        if choice == 4:
            continue
        if choice < 4:
            res[left] += 4 - choice
        else:
            res[right] += choice - 4
    for ques in ['RT','CF','JM','AN']:
        if res[ques[0]] >= res[ques[1]]:
            ans += ques[0]
        elif res[ques[0]] < res[ques[1]]:
            ans += ques[1]
    return ans


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))