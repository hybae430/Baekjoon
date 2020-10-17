dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    global res
    q.append((y, x))
    visited.append((y, x))

    while q:
        y, x = q.pop(0)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in visited and maze[ny][nx] == '1':
                q.append((ny, nx))
                visited.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1
                if (ny, nx) == (N - 1, M - 1):
                    res = dist[ny][nx]
                    return

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
dist = [[0] * M for _ in range(N)]
dist[0][0] = 1
q, visited = [], []
res = 0
bfs(0, 0)
print(res)