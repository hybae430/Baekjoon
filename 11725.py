# 트리의 부모 찾기
import sys
# 재귀깊이 늘리기
sys.setrecursionlimit(10**9)

def dfs(node):
    child = tree[node]
    for c in child:
        if not visited[c]:
            parent[c] = node
            visited[c] = True
            dfs(c)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
visited = [False, True] + [False] * (N - 1)
parent = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
for i in range(2, N + 1):
    print(parent[i])