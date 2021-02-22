# from collections import deque
# n,k = list(map(int,input().split()))
# array = [list(map(int,input().split())) for i in range(n)]
# s,a,b = list(map(int,input().split()))
# queue = deque([])
# stack = []
# for i in range(n):
#     for j in range(n):
#         if array[i][j] != 0:
#             stack.append((i,j,array[i][j],1))
# stack.sort(key = lambda x: x[2])
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]
# for e in stack:
#     queue.append(e)
# time = 0
# while queue:
#     x,y,v,t = queue.popleft()
#     if t > s:
#         break
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 0:
#             array[nx][ny] = v
#             queue.append((nx,ny,v,t+1))
# # print(array)
# print(array[a-1][b-1])
u = '12345'-'123'
print(u)