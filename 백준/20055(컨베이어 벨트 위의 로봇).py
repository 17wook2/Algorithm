from collections import deque
n,k = list(map(int,input().split()))
a = deque(list(map(int,input().split())))
robot = deque([0] * n)
result = 0

while True:
    a.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for i in range(n-2,-1,-1):
            if robot[i] == 1 and robot[i+1] == 0 and a[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                a[i+1] -= 1
            robot[-1] = 0
    if robot[0] == 0 and a[0] >= 1:
        robot[0] = 1
        a[0] -= 1
    result += 1
    if a.count(0) >= k:
        break

print(result)