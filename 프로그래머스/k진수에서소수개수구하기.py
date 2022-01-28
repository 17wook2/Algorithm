import math
def solution(n, k):
    answer = 0
    nq = changenumber(n,k)
    numbers = nq.split('0')
    for number in numbers:
        if checkprime(number):
            answer += 1
    return answer

def checkprime(n):
    if len(n) == 0:
        return False
    n = int(n)
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def changenumber(n,k):
    ans = ''
    while n > 0:
        n,mod = divmod(n,k)
        ans += str(mod)
    ans = ans[::-1]
    return ans