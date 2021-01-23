import functools
def compare(a,b):
    f = a+b
    b = b+a
    return (int(f) > int(b)) - (int(f) < int(b))  # f가 크면 양수, b가 크면 음수, 같으면 0 
    # 바꾸어야 하면 음수, 같으면 0

def solution(numbers):
    n = [str(x) for x in numbers] # 문자열로 바꾸기
    n = sorted(n, key = functools.cmp_to_key(compare), reverse = True)
    answer = str(int(''.join(n)))

    return answer