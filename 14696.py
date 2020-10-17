# 딱지 (IM 대비문제 20)
import sys

def match(A, B, i):
    global ans
    if i == 0:
        ans = 'D'
    elif A.count(i) == B.count(i):
        match(A, B, i - 1)
    elif A.count(i) > B.count(i):
        ans = 'A'
    else:
        ans = 'B'

N = int(sys.stdin.readline())
for n in range(N):
    A = list(map(int, sys.stdin.readline().split()))
    A.pop(0)
    B = list(map(int, sys.stdin.readline().split()))
    B.pop(0)
    ans = ''
    match(A, B, 4)
    print(ans)