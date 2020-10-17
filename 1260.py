def dfs(y):
    print(y, end=" ")
    visitedD[y] = True

    for i in range(1, N + 1):
        if graph[y][i] and not visitedD[i]:
            dfs(i)

def bfs(y):
    Q.append(y)
    visitedB.append(y)

    while Q:
        x = Q.pop(0)
        print(x, end=" ")
        for i in range(1, N + 1):
            if graph[x][i] and i not in visitedB:
                Q.append(i)
                visitedB.append(i)

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visitedD = [False] * (N + 1)
visitedB, Q = [], []

for i in range(M):
    f, t = map(int, input().split())
    graph[f][t] = graph[t][f] = 1   #양방향

dfs(V)
print()
bfs(V)