n,k = map(int,input().split())
numbers = list(map(int,input()))
stack = []
for number in numbers:
    if len(stack) == 0:
        stack.append(number)
    else:
        # 교체
        while len(stack) > 0 and stack[-1] < number and k != 0:
            k -= 1
            stack.pop()
        stack.append(number)
for i in range(k):
    stack.pop()
stack = list(map(str,stack))
# print(stack)
answer = ''.join(stack)
print(int(answer))