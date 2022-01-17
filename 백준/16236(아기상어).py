import math
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

exp = 0
answer = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            start = [i,j]
            arr[i][j] = 2

def bfs(x,y):
    visited = [[0 for i in range(n)] for i in range(n)]
    visited[x][y] = 1
    

while True:
    x,y = start[0], start[1]



def findfish(fish):
    global shark
    x,y,w,ate = shark
    distance = math.inf
    candidate = []
    for f in fish:
        fx,fy,fw = f
        if w <= fw:
            continue
        else:
            d = abs(x-fx) + abs(y-fy)
            if distance >= d:
                candidate.append((fx,fy))
                distance = d
    # print(candidate)
    if candidate != []:
        candidate.sort(key = lambda x: (x[0],x[1]))
        return candidate[0]
    else:
        return (-1,-1)

dx = [-1,-1,0,0]
dy = [0,0,-1,1]
def move():
    global shark
    global fish
    while True:
        fx,fy = findfish(fish)
        # print(fx,fy)
        x,y,w,ate = shark
        stack = []
        if fx == -1 and fy == -1:
            return
        else:
            stack.append((x,y))
            visited = [[0 for i in range(n)] for i in range(n)]
            dist = [[0 for i in range(n)] for i in range(n)]
            while stack:
                # print(stack)
                a,b = stack.pop()
                if a == fx and b == fy: ## 위치 찾은경우
                    answer += dist[fx][fy]
                    print(fish)
                    fish.remove((fx,fy))
                    if w == ate + 1:
                        shark = (a,b,w+1,0)
                    else:
                        shark = (a,b,w,ate+1)
                    break
                else:
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n and w >= arr[nx][ny] and not visited[nx][ny]:
                                visited[nx][ny] = 1
                                stack.append((nx, ny))
                                dist[nx][ny] = dist[x][y] + 1

move()
print(answer)




num_list = []
even_list = []; mul_of_3_list=[]; mul_of_5_list=[];

def get_number():
    while True:
        num = input("입력 자료 생성을 위하여 양의 정수를 입력해 주세요!")
        if num in ['Q','q']:
            break;
        num_list.append(int(num))

def classify_number():
    for i in num_list:
        if i % 2 == 0:
            even_list.append(i)
        elif i % 3 == 0:
            mul_of_3_list.append(i)
        elif i % 5 == 0:
            mul_of_5_list.append(i)

get_number()
classify_number()

print("짝수" , even_list)
print("3의 배수", mul_of_3_list)
print("5의 배수", mul_of_5_list)



