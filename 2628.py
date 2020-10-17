# 종이자르기 (IM 대비문제 14)
N, M = map(int, input().split())
K = int(input())
v, h = [0, N], [0, M]

for i in range(K):
    d, num = map(int, input().split())
    if d == 0:
        h.append(num)
    else:
        v.append(num)

v = sorted(v)
h = sorted(h)

maxv, maxh = 0, 0
for i in range(len(v) - 1):
    if maxv < v[i + 1] - v[i]:
        maxv = v[i + 1] - v[i]

for i in range(len(h) - 1):
    if maxh < h[i + 1] - h[i]:
        maxh = h[i + 1] - h[i]

print(maxv * maxh)