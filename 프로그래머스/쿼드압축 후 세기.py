from itertools import chain
def solution(arr):
    answer = []
    # 각각의 사각형에 대해 분할정복 4개로 쪼갬
    answer = divideandconquer(arr)

    return [answer.count(0), answer.count(1)]

def divideandconquer(arr):
    arr_len = len(arr)
    bound = len(arr)//2
    arr_sum = sum(chain(*arr))
    if arr_len == 1: # 최소단위이면
        return [arr[0][0]]
    elif arr_sum == arr_len*arr_len: #모두 1이면
        return [1]
    elif arr_sum == 0: #모두 0이면
        return [0]
    div0,div1,div2,div3 = (
    [ar[0:bound] for ar in arr[0:bound]],
    [ar[0:bound] for ar in arr[bound:]],
    [ar[bound:] for ar in arr[0:bound]],
    [ar[bound:] for ar in arr[bound:]]
    )

    result = divideandconquer(div0) + divideandconquer(div1) + divideandconquer(div2) + divideandconquer(div3)
    result = list(chain(result))
    return result