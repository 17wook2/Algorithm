answer = 0
n = 0
l = [-1] * 20
r = [-1] * 20
visited = [0] * (1 << 17)


def solution(info, edges):
    global n
    for edge in edges:
        a, b = edge
        if l[a] == -1:
            l[a] = b
        else:
            r[a] = b
    n = len(info)
    tracking(1, info)
    return answer


def tracking(state, info):
    global answer
    if visited[state]:
        return
    visited[state] = 1
    wolf = 0
    sheep = 0
    for i in range(n):
        if state & (1 << i):
            if info[i]:
                wolf += 1
            else:
                sheep += 1
    if wolf >= sheep:
        return
    answer = max(answer, sheep)

    for i in range(n):
        if state & (1 << i):
            if l[i] != -1:
                t = state | (1 << l[i])
                tracking(t, info)
            if r[i] != -1:
                t = state | (1 << r[i])
                tracking(t, info)


