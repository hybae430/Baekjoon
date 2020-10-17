# 자리 배정 (IM 대비문제 9)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
else:
    hall = [[0] * C for _ in range(R)]
    d, y, x, idx = 0, R - 1, 0, 1

    while True:
        hall[y][x] = idx
        if idx == K:
            break
        idx += 1
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < R and 0 <= nx < C and not hall[ny][nx]:
            y, x = ny, nx
        else:
            d = (d + 1) % 4
            y, x = y + dy[d], x + dx[d]
    print(x + 1, R - y)