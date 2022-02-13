import math

cnt = 0
card = [[], [], [], [], [], [], []]
ans = 9999999


def getdist(x, y, cur_x, cur_y):
    rtn = 0
    if abs(cur_x - x) >= 1:  # 커서와 거리 차이가 한칸이면
        rtn += 1
    if abs(cur_y - y) >= 1:
        rtn += 1
    return rtn


def dfs(idx, match, visited, x, y, d):
    global ans
    if match == cnt:
        print(visited, x, y, d)
        ans = min(ans, d)
        return
    clx, cly = card[idx][0]
    crx, cry = card[idx][1]

    ld = getdist(x, y, clx, cly)
    rd = getdist(x, y, crx, cry)
    lrd = getdist(clx, cly, crx, cry)
    for i in range(1, cnt + 1):
        if visited[i]:
            continue
        else:
            visited[i] = 1
            dfs(i, match + 1, visited, clx, cly, d + rd + lrd)
            dfs(i, match + 1, visited, crx, cry, d + ld + lrd)


def solution(board, r, c):
    global cnt, ans
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cnt += 1
                card[board[i][j]].append((i, j))
    cnt //= 2
    for i in range(1, cnt + 1):
        v = [0] * (cnt + 1)
        v[i] = 1
        dfs(i, 1, v, r, c, 0)  ## 시작점, 맞춘갯수, 방문처리, 현재좌표, 움직인수
    ans += (cnt * 2)
    return ans