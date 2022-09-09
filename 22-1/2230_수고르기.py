# 2230_수고르기
# 2022-06-07

"""
2003번 수들의합2와 같이 구간을 정해주고 그 구간과 목표값을 비교해나가기
start와 end 값을 어떤 조건에서 바꿀지가 가장 중요함
문제에서 최솟값이 m이상이라는 조건을 주기 때문에 m을 기준으로 조건나눠주기

pypy3 => 208ms
"""


def check(lst, n, m):
    start, end = 0, 1
    ans = 2e9+1

    while end < n:
        if lst[end] - lst[start] < m:
            end += 1
            continue

        if lst[end] - lst[start] == m:
            return m

        ans = min(ans, lst[end] - lst[start])
        start += 1

    return ans


n, m = map(int, input().split())
lst = [0] * n
for i in range(n):
    lst[i] = int(input())

res = check(sorted(lst), n, m)
print(res)
