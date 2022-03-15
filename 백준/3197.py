from collections import deque
r,c = map(int,input().split())
arr = []
for i in range(r):
    arr.append(list(input().split()))
print(arr)

queue = deque([])
