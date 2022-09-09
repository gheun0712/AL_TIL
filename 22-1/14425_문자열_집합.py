# 14425_문자열_집합
# 2022-05-03

"""
단순하게 안에만 있는지 확인하면 시간초과 나오는 문제
딕셔너리를 활용해서 풀어보았음
주어진 집합에는 중복 경우가 없기 때문에 딕셔너리에 넣어줌
그리고 m개를 확인하면서 값이 존재하면 1씩 카운팅 올려주기

pypy3 => 273ms
python3 => 152 ms
"""

from sys import stdin

N, M = map(int, input().split())
dic = {}
cnt = 0

for _ in range(N):
    dic[stdin.readline().strip()] = True

for _ in range(M):
    if stdin.readline().strip() in dic:
        cnt += 1

print(cnt)


