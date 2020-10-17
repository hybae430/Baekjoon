def bfs(y):
    Q.append(y)
    visited.append(y)

    while Q:
        x = Q.pop(0)
        for i in range(1, C + 1):
            if graph[x][i] and i not in visited:
                Q.append(i)
                visited.append(i)

C = int(input())
N = int(input())
graph = [[0] * (C + 1) for _ in range(C + 1)]
Q, visited = [], []

for i in range(N):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

bfs(1)
print(len(visited) - 1)