from collections import deque
N = int(input())
array = []
house = []
for i in range(N):
    lst = list(map(int,input()))
    array.append(lst)
# print(*array)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for x in range(len(array)):
    for y in range(len(array[0])):
        if array[x][y] == 0:
            continue
        else:
            deq = deque([])
            deq.append((x,y))
            answer = 0
            while deq:
                t_x,t_y = deq.popleft()
                answer += 1
                array[t_x][t_y] = 0
                for i in range(4): # 상하좌우
                    nx = t_x+dx[i]
                    ny = t_y+dy[i]
                    if  nx < 0 or ny < 0 or nx >= len(array) or ny >= len(array[0]) or array[nx][ny] == 0:
                        continue
                    else:
                        array[nx][ny] = 0
                        deq.append((nx,ny))
            house.append(answer)
house.sort()
print(len(house))
for i in range(len(house)):
    print(house[i])