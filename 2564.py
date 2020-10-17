# 경비원 (IM 대비문제 5)
def dist(d, num):
    if d == 1:      # 북
        return num
    elif d == 2:    # 남
        return C + R + C - num
    elif d == 3:    # 서
        return C + R + C + R - num
    elif d == 4:    # 동
        return C + num

C, R = map(int, input().split())
h_list = []
total = (C + R) * 2
T = int(input())

for i in range(T + 1):
    i, num = map(int, input().split())
    h_list.append(dist(i, num))
tmp = h_list.pop()

ans = 0
for i in range(T):
    ans += min(abs(h_list[i] - tmp), total - abs(h_list[i] - tmp))
print(ans)