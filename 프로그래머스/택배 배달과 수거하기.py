def solution(cap, n, deliveries, pickups):
    global idx, d_idx, p_idx
    idx = n - 1
    while idx >= 0 and deliveries[idx] == 0 and pickups[idx] == 0:
        idx -= 1
    ans = 0
    d_idx = idx;
    p_idx = idx

    def go():
        global idx, d_idx, p_idx
        cnt = 0
        while d_idx >= 0 and cnt + deliveries[d_idx] <= cap:
            cnt += deliveries[d_idx]
            deliveries[d_idx] = 0
            d_idx -= 1
        if cnt + deliveries[d_idx] > cap:
            deliveries[d_idx] -= (cap - cnt)
            cnt = cap
        cnt = 0
        while p_idx >= 0 and cnt + pickups[p_idx] <= cap:
            cnt += pickups[p_idx]
            pickups[p_idx] = 0
            p_idx -= 1
        if cnt + pickups[p_idx] > cap:
            pickups[p_idx] -= (cap - cnt)
            cnt = cap
        idx = max(d_idx, p_idx)
        return idx

    while idx >= 0:
        ans += 2 * (idx + 1)
        go()

    return ans


