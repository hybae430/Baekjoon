dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def bfs(y, x):
    q.append((y, x))
    visited.append((y, x))

    while q:
        y, x = q.pop(0)
        town[y][x] = '0'
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited and town[ny][nx] != '0':
                q.append((ny, nx))
                visited.append((ny, nx))

N = int(input())
town = [list(input()) for _ in range(N)]
q, res = [], []
for i in range(N):
    for j in range(N):
        if town[i][j] != '0':
            visited = []
            bfs(i, j)
            res.append(len(visited))

res = sorted(res)
print(len(res))
for i in res:
    print(i)