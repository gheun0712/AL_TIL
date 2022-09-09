# 14501_퇴사
# 2022-03-31


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
# 금액만 뽑아낸 리스트
pay = list(map(lambda x: x[1], lst))

for i in range(N):
    # 날짜 오버되는건 그냥 노룩패스
    if i + lst[i][0] > N:
        pay[i] = 0
        continue

    for j in range(i + lst[i][0], N):
        # 앞선 페이와 현재페이를 비교하고 해당 값을 pay 리스트에 저장
        # 이와 같은 과정을 통해서 pay에는 합산된 pay가 계속해서 저장
        if pay[i] + lst[j][1] > pay[j]:
            pay[j] = pay[i] + lst[j][1]

print(max(pay))
