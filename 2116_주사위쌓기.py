# 2116_주사위쌓기
# 2022-02-19


def my_max(lst):
    num = 0
    for k in lst:
        if num < k:
            num = k
    return num


N = int(input())
dice = []
for _ in range(N):
    dice.append(list(map(int, input().split())))

# top과 bottom이 서로 대치되는 dict 만들어주기
top_bottom = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
ans = 0

# 첫 번째 주사위를 고정해준뒤에 차근차근 쌓아주기!
for i in range(6):
    max_num_lst = []
    origin_dice = [1, 2, 3, 4, 5, 6]  # 원래 주사위는 6까지 있으니까 ㅎㅎ
    origin_dice.remove(dice[0][i])  # 주사위 아랫면 제거
    top = dice[0][top_bottom[i]]  # 윗면 값 뭐게용
    origin_dice.remove(top)  # 없앨게용
    max_num_lst.append((my_max(origin_dice)))

    for j in range(1, N):
        origin_dice = [1, 2, 3, 4, 5, 6]
        origin_dice.remove(top)  # top이 현재 주사위에선 bottom
        top = dice[j][top_bottom[dice[j].index(top)]]  # bottom에 대치되는 top 찾기
        origin_dice.remove(top)  # 없애볼게용
        max_num_lst.append(my_max(origin_dice))

    max_num = sum(max_num_lst)
    if ans < max_num:
        ans = max_num

print(ans)
