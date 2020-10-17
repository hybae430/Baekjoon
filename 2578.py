# 빙고 (IM 대비문제 3)
def isBingo(mat):
    global b_cnt

    for i in range(5):  # 가로
        cnt = 0
        for j in range(5):
            if mat[i][j]:
                cnt += 1
        if cnt == 5:
            b_cnt += 1
    for j in range(5):  # 세로
        cnt = 0
        for i in range(5):
            if mat[i][j]:
                cnt += 1
        if cnt == 5:
            b_cnt += 1
    cnta, cntb = 0, 0
    for i in range(5):  # 대각선
        for j in range(5):
            if i == j and mat[i][j]:
                cnta += 1
            if 4 - i == j and mat[i][j]:
                cntb += 1
    if cnta == 5:
        b_cnt += 1
    if cntb == 5:
        b_cnt += 1

bingo = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
matrix = [[False] * 5 for _ in range(5)]

cnt, b_cnt = 0, 0
for i in range(5):
    for j in range(5):
        cnt += 1
        found = False
        for x in range(5):
            for y in range(5):
                if call[i][j] == bingo[x][y]:
                    found = True
                    matrix[x][y] = True
                if found:
                    break
            if found:
                break
        isBingo(matrix)
        if b_cnt >= 3:
            break
        else:
            b_cnt = 0
    if b_cnt >= 3:
        break
    else:
        b_cnt = 0

print(cnt)