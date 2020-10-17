# 줄 세우기 (IM 대비문제 2)
N = int(input())
q = [1]
ticket = list(map(int, input().split()))

for i in range(1, len(ticket)):
    if ticket[i] == 0:
        q.append(i + 1)
    elif i == ticket[i]:
        q.insert(0, i + 1)
    else:
        q.insert(i - ticket[i], i + 1)

for i in q:
    print(i, end=" ")