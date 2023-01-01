n = int(input())
op = list(input().split())
visited = [0]*10
arr = [-1]*10
first = ''
end = ''
def go(idx,cnt):
    global first,end
    if cnt == n+1:
        res = ''
        for i in range(n+1):
            res += str(arr[i])
        if first == '': first = res
        end = res
        return
    for i in range(10):
        if not visited[i]:
            if idx > 0:
                if op[idx-1] == '<' and arr[idx-1] < i:
                    arr[idx] = i
                    visited[i] = 1
                    go(idx+1,cnt+1)
                    arr[idx] = -1
                    visited[i] = 0
                elif op[idx-1] == '>' and arr[idx-1] > i:
                    arr[idx] = i
                    visited[i] = 1
                    go(idx+1, cnt+1)
                    arr[idx] = -1
                    visited[i] = 0
            else:
                arr[idx] = i
                visited[i] = 1
                go(idx+1,cnt+1)
                arr[idx] = -1
                visited[i] = 0
go(0,0)
print(end)
print(first)