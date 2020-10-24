# N과 M(7)

import sys
N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
out = []  # 출력 내용

def solve(depth, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력
        return
    for i in range(len(arr)):
        out.append(arr[i])  # 탐사 내용
        solve(depth + 1, N, M)
        out.pop()

solve(0, N, M)