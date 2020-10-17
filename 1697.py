from collections import deque

def dfs(n):
    if n == K:
        return 0

    q.append((n, 0))

    while q:
        node, time = q.popleft()
        choice = [node + 1, node - 1, node * 2]
        for c in choice:
            if 0 <= c <= 100000 and not visited[c]:
                if c == K:
                    return time + 1
                else:
                    visited[c] = True
                    q.append((c, time + 1))

N, K = map(int, input().split())
q, visited = deque(), [False] * 100001

print(dfs(N))