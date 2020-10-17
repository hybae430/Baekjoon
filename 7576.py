import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(q):
    days = -1

    while q:
        days += 1

        for n in range(len(q)):
            y, x = q.popleft()

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and box[ny][nx] == 0:
                    box[ny][nx] = box[y][x] + 1
                    q.append((ny, nx))

    for b in box:
        if 0 in b:
            return -1
    return days

M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q, dist = deque(), [[0] * M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            q.append((y, x))

print(bfs(q))