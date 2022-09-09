# 17219_비밀번호_찾기
# 2022-04-20

"""
백준 클래스를 위한 문제!
스트링 일치하는 곳 찾아주기
"""

N, M = map(int, input().split())

info = {}

for _ in range(N):
    x, y = input().split()
    info[x] = y

for _ in range(M):
    print(info[input().rstrip()])