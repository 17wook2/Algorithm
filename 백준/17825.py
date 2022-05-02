import sys
sys.setrecursionlimit(10**5)
arr = list(map(int,input().split()))
graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
ans = 0
def move(idx,cnt):
    if len(graph[idx]) == 1:
        for i in range(cnt):
            idx = graph[idx][0]
    else:
        for i in range(cnt):
            idx = graph[idx][-1]
    return idx
def dfs(depth,res,idxs):
    global ans
    if depth == 10:
        ans = max(ans,res)
        return
    for i in range(4):
        if idxs[i] == 32: ## 도착 한 말 일때
            continue
        t = move(idxs[i],arr[depth])
        if t == 32:
            tmp = idxs[i]
            idxs[i] = t
            dfs(depth+1,res ,idxs)
            idxs[i] = tmp
            continue
        if t < 32 and t not in idxs:
            tmp = idxs[i]
            idxs[i] = t
            dfs(depth+1,res + score[t],idxs)
            idxs[i] = tmp

dfs(0,0,[0,0,0,0])
print(ans)