# 11441_합_구하기
# 2022-05-30

"""
주어진 구간 내 숫자들의 합 구하기 문제
누적함을 저장해놓고 구간을 확인하고 앞 누적구간을 빼준다

Ai+Ai+1+ ... +Aj-1+Aj 일떄, Si = A1+A2+...+Ai이면
Sj - S(i-1)로 표현 가능

Pypy3 => 324ms
Python3 => 4512ms
"""

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
m_lst = [list(map(int, input().split())) for _ in range(m)]
temp = [lst[0]]

for i in range(1, n):
    temp.append(temp[-1]+lst[i])

for i, j in m_lst:
    if i == 1:
        print(temp[j-1])
    else:
        print(temp[j-1]-temp[i-2])