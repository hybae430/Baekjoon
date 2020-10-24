# N과 M(5)

import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)
visited = [False] * N
out = []  # 출력 내용
results = []

def solve(depth, N, M):
    if depth == M:  # 탈출 조건
        a = ' '.join(map(str, out))  # list를 str으로 합쳐 출력
        results.append(a)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            out.append(arr[i])  # 탐사 내용
            solve(depth + 1, N, M)
            visited[i] = False
            out.pop()

solve(0, N, M)
for i in range(len(results)):
    print(results[i])