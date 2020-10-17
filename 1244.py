# 스위치 켜고 끄기 (IM 대비문제 13)

N = int(input())
sw = list(map(int, input().split()))
s_N = int(input())

def switch(n):
    if n == 0:
        return 1
    else:
        return 0

for n in range(s_N):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num - 1, N, num):
            sw[i] = switch(sw[i])
    else:
        st, end = num - 1, num
        for i in range(1, num):
            if num + i - 1 < N:
                if sw[num - i - 1] != sw[num + i - 1]:
                    break
                else:
                    st, end = num - i - 1, num + i
        for i in range(st, end):
            sw[i] = switch(sw[i])

for i in range(len(sw)):
    if i % 20 == 0 and i != 0:
        print()
    print(sw[i], end=" ")