from collections import deque
n,w,l = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr = deque(arr)
bridge = deque([0]*w)

def go():
    move = 0
    while bridge:
        move += 1
        bridge.popleft()
        if arr:
            if sum(bridge) + arr[0] > l:
                bridge.append(0)
            else:
                bridge.append(arr.popleft())
    return move

print(go())
