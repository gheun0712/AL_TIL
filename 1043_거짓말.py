# 1043_거짓말
# 2022-05-19

"""
파티의 수 만큼 반복해서 탐색하기 => 진실을 아는 사람이 포함되어 있는 파티 찾기
모든 파티를 확인해서 진실을 아는 사람이 더 생긴다면 다시 반복해야함

1. 파티 참여자 중 진실을 아는 사람 있는지 확인
2. 진실 아는 자가 있으면 진실을 말한 뒤 진실 집합에 포함시키기
3. 다시 반복이 끝나고 난 뒤 거짓말쟁이 코스프레 할 파티의 수 출력

거짓말쟁이일 때에는 0 진실쟁이일 때에는 1
"""

import sys

n, m = map(int, sys.stdin.readline().split())
know = set(map(int, sys.stdin.readline().split()[1:]))  # 진실 아는 사람 수

party = []
for _ in range(m):
    party.append(set(map(int, sys.stdin.readline().split()[1:])))

cnt = [0] * m

for _ in range(m):
    for x, y in enumerate(party):
        # 파티 참여자와 진실을 아는 사람이 교집합 이면
        if know & y:
            # 진실을 말해야겠죠
            cnt[x] = 1
            # 진실을 아는 사람을 추가해줍시당
            know = know | y

print(cnt.count(0))
