def check():
    if ((ord(ans[0][4]) - 64) + (ord(ans[1][3]) - 64) + (ord(ans[2][2]) - 64) + (ord(ans[3][1]) - 64) != 26): return False;
    if ((ord(ans[0][4]) - 64) + (ord(ans[1][5]) - 64) + (ord(ans[2][6]) - 64) + (ord(ans[3][7]) - 64) != 26): return False;
    if ((ord(ans[1][1]) - 64) + (ord(ans[1][3]) - 64) + (ord(ans[1][5]) - 64) + (ord(ans[1][7]) - 64) != 26): return False;
    if ((ord(ans[3][1]) - 64) + (ord(ans[3][3]) - 64) + (ord(ans[3][5]) - 64) + (ord(ans[3][7]) - 64) != 26): return False;
    if ((ord(ans[4][4]) - 64) + (ord(ans[3][3]) - 64) + (ord(ans[2][2]) - 64) + (ord(ans[1][1]) - 64) != 26): return False;
    if ((ord(ans[4][4]) - 64) + (ord(ans[3][5]) - 64) + (ord(ans[2][6]) - 64) + (ord(ans[1][7]) - 64) != 26): return False;
    return True;
def dfs(idx,n):
    global complete
    if complete:
        return
    if n == cnt:
        if check() and not complete:
            complete = True
            for row in ans:
                print(''.join(row))
            print()
            return
    for i in range(12):
        if visited[i]: continue
        visited[i] = 1
        x,y = arr[idx]
        ans[x][y] = chr(65+i)
        dfs(idx+1,n+1)
        visited[i] = 0
        ans[x][y] = '.'


arr = []
visited = [0]*13
complete = False
cnt = 0
ans = []
for i in range(5):
    lst = list(input())
    ans.append(lst)
    for j in range(len(lst)):
        if 'A' <= lst[j] <= 'L':
            visited[ord(lst[j])-ord('A')] = 1
        elif lst[j] == 'x':
            arr.append((i,j))
            cnt += 1
dfs(0,0)




