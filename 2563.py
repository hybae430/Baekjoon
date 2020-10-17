# 색종이 (IM 대비문제 4)
N = int(input())
paper = [[0] * 100 for _ in range(100)]
for n in range(N):
    x, y = map(int, input().split())
    for i in range(x - 1, x + 9):
        for j in range(y - 1, y + 9):
            paper[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)