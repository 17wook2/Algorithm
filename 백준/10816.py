n = int(input())
hold = list(map(int,input().split()))
m = int(input())
acq = list(map(int,input().split()))
hold_dict = {}
for i in hold:
    if i not in hold_dict:
        hold_dict[i] = 1
    else:
        hold_dict[i] += 1
for i in acq:
    if i not in hold_dict:
        print(0,end=' ')
    else:
        print(hold_dict[i],end=' ')




