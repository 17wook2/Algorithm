def solution(number, k):
    answer = ''
    stack = [number[0]]
    for i in number[1:]:
        while len(stack)>0 and stack[-1]< i and k>0:
            stack.pop()
            k-=1
        stack.append(i)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

#https://scarletbreeze.github.io/articles/2019-07/pythonKit%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4(4)%ED%83%90%EC%9A%95%EB%B2%95%ED%81%B0%EC%88%98 참고
