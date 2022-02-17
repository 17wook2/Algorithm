import heapq
import math
distance = [[math.inf]*1024 for i in range(1004)]
adj = [[] for i in range(1004)]
adjrev = [[] for i in range(1004)]
trapidx = [-1]*1004
def bitmask(state,idx):
    return (1 << trapidx[idx]) & state

def solution(n, start, end, roads, traps):

    for road in roads:
        adj[road[0]].append((road[1],road[2]))
        adjrev[road[1]].append((road[0],road[2]))

    for i in range(len(traps)):
        trapidx[traps[i]] = i

    heap = []
    distance[start][0] = 0
    heapq.heappush(heap, (distance[start][0],start,0))

    while heap:
        val,idx,state = heapq.heappop(heap)
        if idx == end:
            return val
        if distance[idx][state] != val:
            continue

        ## 정방향인 경우 state가 트랩 하나 이동안됨
        for nxt,cost in adj[idx]:
            rev = 0
            if trapidx[idx] != -1 and bitmask(state,idx): rev ^= 1
            if trapidx[nxt] != -1 and bitmask(state,nxt): rev ^= 1
            if rev:
                continue
            nxt_state = state
            if trapidx[nxt] != -1: nxt_state ^= (1 << trapidx[nxt])
            if distance[nxt][nxt_state] > val + cost:
                distance[nxt][nxt_state] = val + cost
                heapq.heappush(heap,(distance[nxt][nxt_state],nxt,nxt_state))

        for nxt,cost in adjrev[idx]:  ## 역방향이면 1개 밟으면 가능
            rev = 0
            if trapidx[idx] != -1 and bitmask(state,idx): rev ^= 1
            if trapidx[nxt] != -1 and bitmask(state,nxt): rev ^= 1
            if not rev:
                continue
            nxt_state = state
            if trapidx[nxt] != -1: nxt_state ^= (1 << trapidx[nxt])
            if distance[nxt][nxt_state] > val + cost:
                distance[nxt][nxt_state] = val + cost
                heapq.heappush(heap,(distance[nxt][nxt_state],nxt,nxt_state))