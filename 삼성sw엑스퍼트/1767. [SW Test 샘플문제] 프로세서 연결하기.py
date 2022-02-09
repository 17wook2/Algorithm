import math
import copy
t = int(input())
for _ in range(t):
    ans = math.inf
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = int(input())
    arr = []
    core = []
    maxcore = 0
    for i in range(n):
        arr.append(list(map(int,input().split())))
    for i in range(1,n-1):
        for j in range(1,n-1):
            if arr[i][j] == 1:
                core.append((i,j))

    def solve(cnt, psum, core, arr, connect):
        global ans
        global maxcore
        if len(core) - cnt + connect < maxcore:
            return
        if cnt == len(core):
            if connect == maxcore:
                ans = min(ans,psum)
            elif connect > maxcore:
                maxcore = connect
                ans = psum
            return
        x, y = core[cnt]
        for i in range(4):
            darr = copy.deepcopy(arr)
            nx = x + dx[i]
            ny = y + dy[i]
            move = 0
            while 0 <= nx < n and 0 <= ny < n:
                if darr[nx][ny] == 1:
                    move = 0
                    break
                else:
                    move += 1
                    darr[nx][ny] = 1
                    nx = nx + dx[i]
                    ny = ny + dy[i]
            if move == 0:
                continue
            else:
                solve(cnt + 1, psum + move,core, darr,connect + 1)
        ## 연결 안한 경우
        solve(cnt + 1,psum,core,arr, connect)

    solve(0, 0, core,arr, 0)
    del core[:]
    print(f"#{_+1} {ans}")

