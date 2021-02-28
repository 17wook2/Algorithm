import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
if m > 0:
    broken = list(input().strip())
# print(broken)
def sol(number):
    for n in number:
        if n in broken:
            return False
    return True
answer = abs(100-n)
try:
    for i in range(1000001):
        if sol(list(str(i))): # 고장난것이 아니면
            answer = min(answer,len(str(i)) + abs(n-i))
    print(answer)
except NameError:
    print(min(abs(100-n),len(str(n))))
