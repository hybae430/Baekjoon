dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def bfs(y, x):
    q.append((y, x))
    visited.append((y, x))

    while q:
        y, x = q.pop(0)
        mount[y][x] = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in visited and mount[ny][nx]:
                q.append((ny, nx))
                visited.append((ny, nx))

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    mount = [[0] * M for _ in range(N)]
    q = []
    cnt = 0
    for i in range(K):
        y, x = map(int, input().split())
        mount[x][y] = 1
    for j in range(N):
        for i in range(M):
            if mount[j][i]:
                visited = []
                cnt += 1
                bfs(j, i)
    print(cnt)
