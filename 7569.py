import sys
from collections import deque

dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(q):
    days = -1

    while q:
        days += 1

        for n in range(len(q)):
            z, y, x = q.popleft()

            for i in range(6):
                ny, nx, nz = y + dy[i], x + dx[i], z + dz[i]
                if 0 <= ny < N and 0 <= nx < M and 0 <= nz < H and box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    q.append((nz, ny, nx))

    for b in box:
        for b1 in b:
            if 0 in b1:
                return -1
    return days

M, N, H = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
q, dist = deque(), [[[0] * M for _ in range(N)] for _ in range(H)]

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                q.append((z, y, x))

print(bfs(q))