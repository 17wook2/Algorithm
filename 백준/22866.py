import math
def solve(start,end,move):
    for i in range(start,end,move):
        while len(stack) > 0 and stack[-1][1] <= arr[i]:
            stack.pop()
        cnt[i] += len(stack)
        if len(stack) > 0:
            dist = abs(stack[-1][0] - i)
            if dist < ans[i][1]:
                ans[i][0] = stack[-1][0]
                ans[i][1] = dist
            elif dist == ans[i][1] and stack[-1][0] < ans[i][0]:
                ans[i][0] = stack[-1][0]
        stack.append([i,arr[i]])
n = int(input())
arr = [0]
arr.extend(list(map(int,input().split())))
ans = [[math.inf, math.inf] for i in range(n+1)]
cnt = [0]*(n+1)
stack = []
solve(1,n+1,1)
stack = []
solve(n,0,-1)
for i in range(1,n+1):
    if cnt[i] != 0:
        print(cnt[i], ans[i][0])
    else:
        print(cnt[i])







