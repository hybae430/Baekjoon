# 참외밭 (IM 대비문제 7)
K = int(input())
c = []
r = []
seq = []

for i in range(6):
    d, num = map(int, input().split())
    if d == 1 or d == 2:
        c.append(num)
    else:
        r.append(num)
    seq.append(num)

seq = seq * 2
area = max(r) * max(c)
cnt = 0
for i, s in enumerate(seq):
    if s == max(r) or s == max(c):
        cnt = 0
    else:
        cnt += 1
    if cnt == 4:
        idx = i

area -= seq[idx - 2] * seq[idx - 1]
print(area * K)