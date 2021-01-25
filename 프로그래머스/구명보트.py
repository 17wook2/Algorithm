from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    deq = deque(people)
    boat = []
    while deq:
        try:
            front = deq.popleft()
            back = deq.pop()
            if front + back > limit:
                deq.append(back)
            answer += 1
        except IndexError:
            answer += 1


    return answer