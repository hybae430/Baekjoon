# 수 이어가기 (IM 대비문제 12)
N = int(input())

ans, ans_list = 0, []
for i in range(N, -1, -1):
    seq = [N]
    tmp = i
    while tmp >= 0:
        seq.append(tmp)
        tmp = seq[len(seq) - 2] - seq[len(seq) - 1]
    if len(seq) > ans:
        ans = len(seq)
        ans_list = seq[:]

print(ans)
print(*ans_list)    # 요소 하나씩 출력