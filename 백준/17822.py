from collections import deque
n,m,t = list(map(int,input().split()))
numbers = []
numbers.append([0])
for i in range(n):
    tmp = list(map(int,input().split()))
    queue = deque(tmp)
    numbers.append(queue)
rt = []
for i in range(t):
    rt.append(list(map(int,input().split())))
def rotate(idx,d,k): ## d 방향으로 k번 옮기는 함수
    for i in range(1,n+1):
        if i % idx == 0: ## i 배수인 원판에 대하여
            if d == 0: ## 시계방향 인 경우 뒤에 있는거 앞으로
                for j in range(k):
                    numbers[i].rotate(1)
            else:
                for j in range(k):
                    numbers[i].rotate(-1)

def remove():
    ## 같은 행끼리 확인
    erase_list = []
    for i in range(1,n+1):
        for j in range(m):
            if j == m-1: ## 같은 행 오른쪽 비교
                if numbers[i][j] != 'x' and numbers[i][j] == numbers[i][0]:
                    erase_list.append((i,j))
                    erase_list.append((i,0))
            else:
                if numbers[i][j] != 'x' and numbers[i][j] == numbers[i][j+1]:
                    erase_list.append((i,j))
                    erase_list.append((i,j+1))
            if i != n and numbers[i][j] != 'x' and numbers[i][j] == numbers[i+1][j]:
                erase_list.append((i, j))
                erase_list.append((i + 1, j))

    erase_list = list(set(erase_list))

    tmp = 0
    k = 0
    if len(erase_list) == 0: ## 인접한것 없다면
        for i in range(1,n+1):
            for j in range(m):
                if numbers[i][j] != 'x':
                    tmp += numbers[i][j]
                    k += 1
        for i in range(1,n+1):
            for j in range(m):
                if numbers[i][j] != 'x':
                    if numbers[i][j] > tmp/k:
                        numbers[i][j] -= 1
                    elif numbers[i][j] < tmp/k:
                        numbers[i][j] += 1
    else:
        for pair in erase_list:
            x,y = pair
            numbers[x][y] = 'x'
# print(numbers)
for r in rt:
    x,d,k = r
    rotate(x,d,k)
    remove()

ans = 0
for i in range(1,n+1):
    for j in range(m):
        if numbers[i][j] != 'x':
            ans += numbers[i][j]
print(ans)
# print(numbers)

