# 트리의 순회

import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
pre = []
pos = [0] * (n + 1)
root = postorder[-1]    # postorder 마지막이 항상 root

for i in range(n):
    pos[inorder[i]] = i

def divide(in_start, in_end, post_start, post_end):
    if post_start <= post_end:
        parents = postorder[post_end]

        print(parents, end=" ")
        p_index = pos[parents]
        l_count = p_index - in_start
        r_count = in_end - p_index

        divide(in_start, in_start + l_count - 1, post_start, post_start + l_count - 1)
        divide(in_end - r_count + 1, in_end, post_end - r_count, post_end - 1)

divide(0, n - 1, 0, n - 1)