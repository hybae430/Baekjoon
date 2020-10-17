import sys

# 방 배정 (IM 대비문제 19)
N, K = map(int, sys.stdin.readline().split())
st = [[0, 0] for _ in range(7)]

for n in range(N):
    sx, yr = map(int, sys.stdin.readline().split())
    st[yr][sx] += 1

cnt = 0
for i in st:
    for j in range(2):
        if i[j] != 0:
            if i[j] % K:
                cnt += i[j] // K + 1
            else:
                cnt += i[j] // K

print(cnt)