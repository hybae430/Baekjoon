# 색종이 (IM 대비문제 18)
import sys
N = int(sys.stdin.readline())
area = [[0] * 101 for _ in range(101)]
idx = 1
for n in range(N):
    X, Y, H, V = map(int, sys.stdin.readline().split())
    for y in range(Y, Y + V):
        for x in range(X, X + H):
            area[y][x] = idx
    idx += 1

for i in range(1, N + 1):
    cnt = 0
    for y in range(101):
        for x in range(101):
            if area[y][x] == i:
                cnt += 1
    print(cnt)