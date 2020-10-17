# 창고 다각형 (IM 대비문제 16)
import sys

N = int(sys.stdin.readline())
area = [0] * 1001
h_max, tmp, ans = 0, 0, 0

for n in range(N):
    x, h = map(int, sys.stdin.readline().split())
    if h_max < h:
        h_max = h
    area[x] = h

idx = 0
for i in range(len(area)):
    if tmp == h_max:
        idx = i
        break
    elif tmp < area[i]:
        tmp = area[i]
    ans += tmp

tmp = 0
for i in range(len(area) - 1, idx - 1, -1):
    if tmp < area[i]:
        tmp = area[i]
    ans += tmp

print(ans)