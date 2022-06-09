from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    ans = len(dist) + 1
    for i in range(length):
        weak.append(n + weak[i])
    per = list(permutations(dist))
    print(per)
    for start in range(length):
        for com in per:
            cnt = 1
            pos = weak[start] + com[cnt - 1]
            for idx in range(start, start+length):
                if pos < weak[idx]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[idx] + com[cnt - 1]
            ans = min(cnt,ans)

    return ans

print(solution(12,[1,5,6,10],[1,2,3,4]))
print(solution(12,[1, 3, 4, 9, 10],[3,5,7]))