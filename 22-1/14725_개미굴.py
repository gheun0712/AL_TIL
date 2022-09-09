# 14725_개미굴
# 2022-05-09

"""
노드 끝까지 쭈욱 들어가니까 신호는 항상 층 순서대로 반환됨
반환된 값을 부모-자식으로 나누어서 저장시켜야함 >> 자식이 다시 부모가 되는 경우도 있음
Key 에는 부모 Value에는 노드의 자식들

PyPy3 => 140ms
Python 3 => 104ms
"""

N = int(input())
dic = {}

for i in range(N):
    arr = list(input().split())
    target = dic
    for j in arr[1:]:
        if j not in target:
            target[j] = {}
        target = target[j]


def find(goal, n):
    target_key = sorted(goal.keys())
    for s in target_key:
        print('--' * n + s)
        find(goal[s], n + 1)


find(dic, 0)
