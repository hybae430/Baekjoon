T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    res = []
    ans = list(map(int, input().split()))
    for i in range(N):
        st = list(map(int, input().split()))
        cnt, score = 0, 0
        for n in range(len(ans)):
            if ans[n] == st[n]:
                cnt += 1
                score += cnt
            else:
                cnt = 0
        res.append(score)

    print('#{} {}'.format(tc, max(res) - min(res)))