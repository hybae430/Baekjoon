# 직사각형 (IM 대비문제 8)
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if (x1 > p2 or x2 > p1) or (y1 > q2 or y2 > q1):            # 왼쪽 아래와 다른 사각형 오른쪽 위 좌표 비교를 통해 절대 만나지 않는 것 확인
        print("d")
    elif (x1 == p2 or x2 == p1) and (y1 == q2 or y2 == q1):
        print("c")
    elif (x1 == p2 or x2 == p1) or (y1 == q2 or y2 == q1):
        print("b")
    else:
        print("a")