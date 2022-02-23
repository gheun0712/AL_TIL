# 2578_빙고
# 2022-02-23


bingo = [list(map(int, input().split())) for _ in range(5)]

# 0-4까지 행, 5-9까지는 열. 10은 우하향 대각선, 11은 좌하향 대각선
# 행변화 감지하면 check_lst 카운팅을 1씩 올려줘서 카운팅 5가 되면 빙고!
check_lst = [0] * 12


call_num = []
for i in range(5):
    call = list(map(int, input().split()))
    for j in call:
        call_num.append(j)

for n in range(25):
    for i in range(5):
        for j in range(5):
            # 사회자가 부른 수랑 빙고랑 체크체크되면 빙고판 해당수를 0으로 변경
            # 체크리스트에 해당 행 혹은 열 혹은 대각선 번호에 해당되는 인덱스 값을 카운팅
            if call_num[n] == bingo[i][j]:
                bingo[i][j] = 0
                check_lst[i] += 1
                check_lst[j + 5] += 1
                # 우하향 대각선
                if i == j:
                    check_lst[10] += 1
                # 좌하향 대각선
                if i + j == 4:
                    check_lst[11] += 1

    bingo_cnt = 0
    for num in range(12):
        # 숫자 바뀐게 5개인걸 찾으면 초기화 시켜주고 빙고 카운트 올리기
        if check_lst[num] == 5:
            # check_lst[num] = 0
            bingo_cnt += 1
    if bingo_cnt >= 3:
        break

print(n+1)