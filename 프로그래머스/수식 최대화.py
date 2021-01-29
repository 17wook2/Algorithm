# 분할정복!! 우선순위 낮은 것 부터 분할
# unsolved
def calc(priority,expression,n):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority,exp,n+1) for exp in expression.split('*')]))
    elif priority[n] == '+':
        res = eval('+'.join([calc(priority,exp,n+1) for exp in expression.split('+')]))
    elif priority[n] == '-':
        res = eval('-'.join([calc(priority,exp,n+1) for exp in expression.split('-')]))
    return str(res)
def solution(expression):
    answer = 0
    operators = [('*','+','-'),('*','-','+'),('+','*','-'),('+','-','*'),('-','*','+'),('-','+','*')]
    for priority in operators:
        res = int(calc(priority,expression,0))
        answer = max(answer, abs(res))
    return answer

