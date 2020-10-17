# 주사위 쌓기 (IM 대비문제 15)
import sys

def find(x):
    if x == 0: return 5
    elif x == 1: return 3
    elif x == 2: return 4
    elif x == 3: return 1
    elif x == 4: return 2
    elif x == 5: return 0

N = int(sys.stdin.readline())
dices, res = [], []

for n in range(N):
    dice = list(map(int, sys.stdin.readline().split()))
    dices.append(dice)

for i in range(6):
    ans = 0
    first = dices[0][i]      # 맨 아래값
    for j in range(len(dices)):
        dice = dices[j]
        op = dice[find(dice.index(first))]
        tmp = dice[:]
        tmp.remove(first)
        tmp.remove(op)
        ans += max(tmp)
        first = op
    res.append(ans)

print(max(res))