def solution(bricks, n, k):
    answer = 0
    x = []
    c = []
    for i in range(1,len(bricks)-1):
        if bricks[i-1] <= bricks[i] and bricks[i] >= bricks[i+1] and bricks[i] != n:
            c.append((i,n-bricks[i]))
    c.sort(key = lambda x:x[1])
    for idx in c:
        if k == 1:
            return answer
        answer += idx[1]
        bricks[idx[0]] = n
        k -= 1
    while k != 1:
        c = []
        for i in range(1,len(bricks)-1):
            if bricks[i] != n and bricks[i-1] != n and bricks[i+1] != n:
                c.append((i,n-bricks[i]))
        c.sort(key = lambda x:x[1])
        r = c[0]
        bricks[r[0]] = n
        answer += r[1]
        k -= 1

    return answer

print(solution([2,2,2,2,2,2],6,3))