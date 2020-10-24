# N과 M(6)

import sys
N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * N
out = []  # 출력 내용

def solve(depth, idx, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력
        return
    for i in range(idx, len(arr)):
        if not visited[i]:
            visited[i] = True
            out.append(arr[i])  # 탐사 내용
            solve(depth + 1, i + 1, N, M)
            visited[i] = False
            out.pop()

solve(0, 0, N, M)