# 수열 (IM 대비문제 17)
import sys

N, K = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
t_max = -10000001
first = sum(tmp[0:K])

for i in range(0, N):
    if first > t_max:
        t_max = first
    if i + K >= N:
        break
    first -= tmp[i]
    first += tmp[i + K]

print(t_max)