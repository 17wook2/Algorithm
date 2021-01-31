import time
[N,B] = list(map(int,input().split()))
mat = [list(map(int,input().split())) for i in range(N)]
def solution(B):
    rtm = [[0 for i in range(N)] for _ in range(N)]
    if B == 1:
        for i in range(N):
            for j in range(N):
                rtm[i][j] = mat[i][j]
    elif B %2 == 1:
        matrix = solution(B//2)
        r = [[0]* N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                r[i][j] = sum(matrix[i][t]*matrix[t][j] for t in range(N)) % 1000
        for i in range(N):
            for j in range(N):
                rtm[i][j] += sum(r[i][t]*mat[t][j] for t in range(N)) % 1000
    else:
        matrix = solution(B//2)
        for i in range(N):
            for j in range(N):
                rtm[i][j] = sum(matrix[i][t]*matrix[t][j] for t in range(N)) % 1000
    for i in range(N):
        rtm[i] = list(map(lambda x:x%1000, rtm[i]))
    return rtm

fmat = solution(B)
for row in fmat:
    print(*row)
