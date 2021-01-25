from itertools import combinations
from functools import reduce
def solution(clothes):
    dict = {}
    for cloth in clothes:
        if cloth[1] in dict:
            dict[cloth[1]] += 1
        else:
            dict[cloth[1]] = 1
    lst = dict.values()
    lst = list(map(lambda x:x+1, lst))

    return multiply(lst) -1

def multiply(lst):
    return reduce(lambda x,y:x*y, lst)