words = []
for i in range(6):
    words.append(input())
visited = [0]*6
ans = []
def check():
    c = []
    temp = [0]*6
    for i in range(1,4):
        idx = visited.index(i)
        c.append(words[idx])
    for i in range(3):
        col = ''
        for j in range(3):
            col += c[j][i]
        for k in range(6):
            if words[k] == col and not visited[k] and not temp[k]:
                temp[k] = 1
                break
    if sum(temp) != 3:
        return False
    res = ''.join(c)
    ans.append(res)
def go(cnt):
    global ans
    if cnt == 4:
        check()
    for i in range(6):
        if not visited[i]:
            visited[i] = cnt
            go(cnt+1)
            visited[i] = 0
go(0)
if len(ans) == 0:
    print(0)
else:
    ans.sort()
    for i in range(0,9,3):
        print(ans[0][i:i+3])