import sys
import copy
from collections import deque
queue = deque([])
queue.append()
input = sys.stdin.readline
n,m,r = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
cmd = list(map(int,input().split()))
for x in cmd:
    if x == 1:
        for i in range(m):
            for k in range(n//2):
                arr[k][i],arr[n-k-1][i] = arr[n-k-1][i],arr[k][i]
    elif x == 2:
        for i in range(n):
            for k in range(m//2):
                arr[i][k], arr[i][m-k-1] = arr[i][m-k-1], arr[i][k]
    elif x == 3:
        arr2 = copy.deepcopy(arr)
        arr = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                arr[i][j] = arr2[n-j-1][i]
        n,m = m,n
    elif x == 4:
        arr2 = copy.deepcopy(arr)
        arr = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                arr[i][j] = arr2[j][m-i-1]
        n,m = m,n
    elif x == 5:
        arr2 = copy.deepcopy(arr)
        for i in range(n):
            for j in range(m):
                if i < n // 2 and j < m // 2:
                    arr[i][j] = arr2[i+n//2][j]
                elif i < n // 2 and j >= m // 2:
                    arr[i][j] = arr2[i][j-m//2]
                elif i >= n // 2 and j >= m // 2:
                    arr[i][j] = arr2[i-n//2][j]
                elif i >= n // 2and j < m//2:
                    arr[i][j] = arr2[i][j-m//2]
    elif x == 6:
        arr2 = copy.deepcopy(arr)
        for i in range(n):
            for j in range(m):
                if i < n // 2 and j < m // 2:
                    arr[i][j] = arr2[i][j+m//2]
                elif i < n // 2 and j >= m // 2:
                    arr[i][j] = arr2[i+n//2][j]
                elif i >= n // 2 and j >= m // 2:
                    arr[i][j] = arr2[i][j-m//2]
                elif i >= n // 2and j < m//2:
                    arr[i][j] = arr2[i-n//2][j]
for row in arr:
    print(*row)

