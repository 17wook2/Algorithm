parent = {}
ans = {}
def func(node,cost): ## seller들에 대해서 func 적용, 아래에서 위로
    if node == '-':
        return
    ref = int(cost * 0.1)
    if ref < 1:
        ans[node] += cost
    else:
        ans[node] += cost-ref
        func(parent[node],ref)
def solution(enroll, referral, seller, amount):
    ## root는 -
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        ans[enroll[i]] = 0
    for i in range(len(seller)):
        func(seller[i],amount[i]*100)
    p = []
    for worker in enroll:
        p.append(ans[worker])
    return p