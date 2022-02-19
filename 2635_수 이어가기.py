# 2635_수이어가기

N = int(input())
count = 0
ans = []
for sec in range(1, N + 1):
    temp = 0  # 최종 카운트 주기 전에 임시로 넣어두긔
    first = N
    third = N - sec  # 3번째 수는 첫번째 수 - 두번째 수
    temp_lst = [first, sec, third]

    # 계속 순환하면서 1,2,3 교체 시켜주려고 했눈뎅 Fail...
    while third >= 0:
        third = sec - third
        sec = first - sec
        first = sec - third
        temp += 1
        temp_lst += [third]

    # count 최대값 구하기
    if count < temp:
        count = temp
        ans = temp_lst

answer = ''
for a in range(len(ans)-1):
    answer += str(ans[a]) + ' '

print(count)
print(answer)
