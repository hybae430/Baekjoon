# 직사각형 네개의 합집합 (IM 대비문제 11)
area = [[0] * 101 for _ in range(101)]
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            area[y][x] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if area[i][j]:
            cnt += 1

print(cnt)