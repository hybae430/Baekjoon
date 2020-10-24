import sys
T = int(sys.stdin.readline())
for tc in range(T):
    n = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    sticker[0][1] += sticker[1][0]
    sticker[1][1] += sticker[0][0]
    for i in range(2, n):
        sticker[0][i] += max(sticker[1][i - 1], sticker[1][i - 2])
        sticker[1][i] += max(sticker[0][i - 1], sticker[0][i - 2])
    print(max(sticker[0][n - 1], sticker[1][n - 1]))