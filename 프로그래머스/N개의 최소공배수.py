def solution(arr):
    answer = 0

    return answer


def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

print(gcd(5,12))