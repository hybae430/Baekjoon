# N과 M(9)

import sys
N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * N
out = []  # 출력 내용

def solve(depth, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, out))) # list를 str으로 합쳐 출력
        return
    over = 0
    for i in range(len(arr)):
        if not visited[i] and over != arr[i]:
            visited[i] = True
            over = arr[i]
            out.append(arr[i])  # 탐사 내용
            solve(depth + 1, N, M)
            out.pop()
            visited[i] = False

solve(0, N, M)