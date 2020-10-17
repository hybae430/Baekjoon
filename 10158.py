# 개미 (IM 대비문제 10)
def ant(pos, length):
    d = (pos + t) // length     # 벽에 부딫힌 횟수
    idx = (pos + t) % length    # 개미가 간 거리
    if d % 2 == 0:              # 짝수번 부딫혔으면 그대로 출력
        return idx
    else:                       # 홀수번 부딫혔으면 전체길이에서 빼주기
        return length - idx

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

print(ant(p, w), ant(q, h))
