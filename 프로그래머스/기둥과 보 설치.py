def isstable(n,answer):
    for frame in answer:
        x,y,a = frame # 위치 , 설치종류
        if a == 0: # 기둥일경우
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            else:
                return False
        elif a == 1: # 보일경우
            if [x+1,y-1,0] in answer or [x,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False
    return True
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,a,b =  frame
        if b == 0:
            answer.remove([x,y,a])
            if not isstable(n,answer):
                answer.append([x,y,a])
        elif b == 1:
            answer.append([x,y,a])
            if not isstable(n,answer):
                answer.remove([x,y,a])
    answer.sort()
    return answer