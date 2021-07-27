import copy
n,m,h = list(map(int,input().split()))
graph = [[0 for i in range(n)] for i in range(h)]
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a-1][b-1] = 1

def check():
    for i in range(n): ## n번줄까지
        start = i
        for j in range(h):
            if graph[j][start]: ## 사다리 시작점를 만났다면
                start += 1
            elif start > 0 and graph[j][start-1]: ## 왼쪽에 사다리가 있다면
                start -= 1
        if i != start:
            return False
    return True

def solve(cnt,x,y):
    global answer
    if check():
        answer = min(answer,cnt)
        return
    elif cnt == 3 or answer <= cnt:
        return
    for i in range(x,h):
        if i == x: ## 같은 가로선에서 더 추가할 수 있는지 먼저 확인
            k = y
        else:
            k = 0
        for j in range(k,n):
            if graph[i][j]:
                continue
            elif j > 0 and graph[i][j-1]:
                continue
            elif j > 0 and not graph[i][j-1]:
                graph[i][j-1] = 1
                solve(cnt+1,i,j+1)
                graph[i][j-1] = 0
answer = 4

solve(0,0,0)
if answer >= 4:
    answer = -1
print(answer)