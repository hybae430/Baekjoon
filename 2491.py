# 수열 (IM 대비문제 6)
N = int(input())
nums = list(map(int, input().split()))

ans, tmpp, tmpm = 0, 0, 0
now = nums[0]
for num in nums:
    if now <= num:  # 증가 경우
        tmpp += 1
    else:
        tmpp = 1

    if now >= num:  # 감소 경우
        tmpm += 1
    else:
        tmpm = 1

    now = num
    if ans < tmpp:
        ans = tmpp
    elif ans < tmpm:
        ans = tmpm

print(ans)