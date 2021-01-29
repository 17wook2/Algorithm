def returntobit(n):
    stack = []
    while n > 0:
        stack.append(n%2)
        n = n//2
    stack = stack[-1::-1]
    return stack
print(returntobit(78))