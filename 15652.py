# N과 M(4)

import sys
N, M = map(int, sys.stdin.readline().split())
out = []  # 출력 내용
results = []

def solve(depth, N, M):
    if depth == M:  # 탈출 조건
        a = ' '.join(map(str, out))  # list를 str으로 합쳐 출력
        results.append(a)
        return
    for i in range(N):
        if not out or out[-1] <= i + 1:
            out.append(i + 1)  # 탐사 내용
            solve(depth + 1, N, M)
            out.pop()

solve(0, N, M)
for i in range(len(results)):
    print(results[i])