def solution(answer,n):
    global count
    if len(answer) == n:
        count += 1
        return 0
    candidate = list(range(n))
    for i in range(len(answer)):
        if answer[i] in candidate:
            candidate.remove(answer[i])
        distancce = len(answer) - i
        if answer[i] + distancce in candidate:
            candidate.remove(answer[i] + distancce)
        if answer[i] - distancce in candidate:
            candidate.remove(answer[i] - distancce)
    if candidate != []:
        for i in candidate:
            answer.append(i)
            solution(answer,n)
            answer.pop()
    else:
        return 0

num = int(input())
count = 0
for i in range(num):
    solution([i],num)

print(count)