from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
hittings = []
def simulate(lineup):
    idx = 0;
    score = 0
    for inning in range(1,n+1):
        b1,b2,b3 = 0,0,0
        cur_out_count = 0
        while cur_out_count < 3:
            player = lineup[idx]
            hit = hittings[inning - 1][player-1]
            if hit == 0: ## 아웃인 경우
                cur_out_count += 1
            elif hit == 1:
                score += b3
                b1,b2,b3 = 1,b1,b2
            elif hit == 2:
                score += (b2 + b3)
                b1,b2,b3 = 0, 1, b1
            elif hit == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif hit == 4:
                score += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            idx = (idx + 1) % 9
    return score

for i in range(n):
    hittings.append(list(map(int,input().split())))
players = [i for i in range(1,10)]
lineups = list(permutations(players,9))
ans = 0
for lineup in lineups:
    if lineup[3] != 1: continue
    ans = max(ans, simulate(lineup))

print(ans)
