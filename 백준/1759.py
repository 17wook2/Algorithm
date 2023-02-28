l,c = list(map(int,input().split()))
arr = list(input().split())
arr.sort()
vowels = ['a','e','i','o','u']
vis = [0]*c
def check():
    a,b = 0,0
    ans = ''
    for i in range(c):
        if vis[i]:
            if arr[i] in vowels: b += 1
            else: a += 1
            ans += arr[i]
    if b >= 1 and a >= 2:
        print(ans)
    return

def go(idx,cnt):
    if cnt == l:
        check()
        return
    for i in range(idx,c):
        if not vis[i]:
            vis[i] = 1
            go(i+1,cnt+1)
            vis[i] = 0
go(0,0)
