def solution(p):
    return returnCorrect(p)

def getUV(p): # u,v 반환
    count = 0
    if p=='':
        return ''
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return p[:i+1], p[i+1:]
def checkCorrect(p): #올바른 문자열인지 확인
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        elif p[i] == ')' and count != 0:
            count -= 1
    return True if count == 0 else False        
def toggle(p):
    tempStr = ''
    for i in p:
        if i =='(':
            tempStr += ')'
        else:
            tempStr += '('
    return tempStr

def returnCorrect(p):
    if p == '':
        return p
    u,v = getUV(p)
    if checkCorrect(u): # 올바른 문자열이면
        return u+returnCorrect(v)
    else:               # 올바른 문자열 아니면
        temp = ''
        temp += '('
        temp += returnCorrect(v)
        temp += ')'
        u = u[1:-1]
        u = toggle(u)
        temp += str(u)
        return temp