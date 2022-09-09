# 14891_톱니바퀴
# 2022-04-10
# 2022-04-12(해결!)
"""
1번 톱니바퀴 기준으로 돌려놓고 그 뒤로 순서대로 톱니바퀴 방향 바꿔주기
N극 S극 구별하는 조건 확인해서 회전시켜주기
기준 톱니바퀴 기준으로 좌측 우측 나누어서 해결해보기!
rotate() 함수 사용해서 방향대로 돌려주는게 포인트
"""
from collections import deque

gear = [deque(map(int, input())) for _ in range(4)]
k = int(input())
lst = deque(list(map(int, input().split())) for _ in range(k))

while lst:
    num, d = lst.popleft()
    num -= 1
    temp_2 = gear[num][2]
    temp_6 = gear[num][6]
    gear[num].rotate(d)
    temp_direction = d

    # 왼쪽
    d = temp_direction
    for i in range(num-1, -1, -1):
        if gear[i][2] != temp_6:
            temp_6 = gear[i][6]
            # 회전 방향대로 회전시켜주고 방향이동
            gear[i].rotate(d*-1)
            d *= -1
        else:
            break

    # 오른쪽
    d = temp_direction
    for i in range(num+1, 4):
        if gear[i][6] != temp_2:
            temp_2 = gear[i][2]
            # 회전 방향대로 회전시켜주고 방향이동
            gear[i].rotate(d*-1)
            d *= -1
        else:
            break

res = 0
for i in range(4):
    if gear[i][0] == 1:
        res += 2**i
print(res)

