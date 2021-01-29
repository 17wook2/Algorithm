N = int(input())
lst = list(map(int,input().split()))
stack = []
answer = [-1]*N
stack.append(0)
for i in range(len(lst)):
    try:
        while lst[stack[-1]] < lst[i]:
            answer[stack.pop()] = lst[i]
    except IndexError:
        pass
    stack.append(i)
print(*answer)
