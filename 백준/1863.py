import sys
input = sys.stdin.readline
n = int(input())
stack = []
ans = 0
for i in range(n):
    x,y = list(map(int,input().split()))
    while len(stack) > 0 and stack[-1] > y:
        ans += 1
        stack.pop()
    if len(stack) > 0 and stack[-1] == y:
        continue
    stack.append(y)

while stack:
    if stack[-1] > 0:
        ans += 1
    stack.pop()
print(ans)