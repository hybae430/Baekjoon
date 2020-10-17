# 일곱난쟁이 (IM 대비문제 1)
def dfs(y, total):
    if total == 100 and visited.count(True) == 7:
        if not ans:     # 한번만 출력
            for i in range(len(heights)):
                if visited[i]:
                    ans.append(heights[i])
        return

    if y >= 9 or total > 100:
        return

    visited[y] = True
    dfs(y + 1, total + heights[y])
    visited[y] = False
    dfs(y + 1, total)

heights = []
for i in range(9):
    heights.append(int(input()))
visited = [False] * len(heights)
ans = []
dfs(0, 0)
ans = sorted(ans)
for a in ans:
    print(a)