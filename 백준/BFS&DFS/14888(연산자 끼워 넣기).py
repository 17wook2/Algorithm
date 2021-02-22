import math
from itertools import permutations
n = int(input())
numbers = list(map(int,input().split()))
operators = list(map(int,input().split()))
county = []
for i in range(4):
    for j in range(operators[i]):
        county.append(i)
candidate = list(permutations(county,n-1))
# print(candidate)
l,s = -math.inf,math.inf
for i in range(len(candidate)):
    answer = numbers[0]
    for j in range(1,len(numbers)):
        if candidate[i][j-1] == 0: # 더하기 일떄
            answer += numbers[j]
        elif candidate[i][j-1] == 1: # 뺴기 일때
            answer -= numbers[j]
        elif candidate[i][j-1] == 2: # 곱하기 일때
            answer *= numbers[j]
        elif candidate[i][j-1] == 3: #나누기 일때
            if answer >= 0:
                temp = answer // numbers[j]
                answer = temp
            else:
                temp = -answer // numbers[j]
                answer = -temp
    l = max(l,answer)
    s = min(s,answer)
print(l)
print(s)

