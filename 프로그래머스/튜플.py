import re
from collections import Counter

def solution(s):
    answer = []
    a = re.findall('\d+', s)
    b = Counter(a)

    return answer